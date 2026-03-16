#!/usr/bin/env python3
"""
Fix teacher photo positions in edushift-samples HTML files.
The `teacher-photo-wrap` CSS class is on the correct div,
but the base64 image DATA may be in the wrong position.
"""

import re
import hashlib
import shutil
from datetime import datetime

ENGLISHROOM_TEACHER_MD5_PREFIX = "d99779422f32"

FILES = [
    "/Users/yossy/edushift-samples/englishroom-a.html",
    "/Users/yossy/edushift-samples/englishroom-b.html",
    "/Users/yossy/edushift-samples/manabiko-a.html",
    "/Users/yossy/edushift-samples/manabiko-b.html",
]

# Pattern: matches <div class="...img-wrap..."><img src="data:image/...;base64,...">
# Captures: group(1)=class attr, group(2)=full src value, group(3)=base64 data
IMG_WRAP_PATTERN = re.compile(
    r'(<div class="([^"]*img-wrap[^"]*)")><img src="(data:image/[^;]+;base64,([^"]+))"'
)


def get_md5(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()


def find_teacher_photo_index_manabiko(matches):
    """
    For manabiko files: teacher photo is ~403KB raw file.
    In base64, 403KB binary ≈ 403*1024*(4/3) chars ≈ 551KB chars.
    But we see sizes: 165KB, 303KB, 75KB, 214KB (in file sizes of base64-decoded).
    The task says ~403KB file. Let's find the largest that could be a portrait.
    Actually the user says "403KB file" - let's check which base64 data decodes to ~403KB.
    base64 chars * 3/4 = decoded bytes
    403*1024 = 412672 bytes -> base64 chars ~= 550229

    From our analysis:
      manabiko-a: sizes 165KB, 303KB, 75KB, 214KB
      manabiko-b: sizes 298KB, 303KB, 75KB, 144KB

    None exactly match 403KB. Let's pick by largest size that's not already in teacher-photo-wrap.
    Actually, re-reading: the 303KB image appears in BOTH manabiko files at position 2 with same MD5.
    The teacher-photo-wrap currently has 75KB. So the 303KB is likely the actual teacher photo.
    """
    # Find index of teacher-photo-wrap div
    teacher_wrap_idx = None
    for i, m in enumerate(matches):
        if "teacher-photo-wrap" in m.group(2):
            teacher_wrap_idx = i
            break

    if teacher_wrap_idx is None:
        return None, None

    # Find the largest image NOT in teacher-photo-wrap - likely the actual teacher photo
    # But we need to identify which one is the teacher.
    # From analysis: 303KB image has same MD5 in both manabiko files - it's a consistent image.
    # The teacher-photo-wrap currently has 75KB.
    # The 303KB (md5=470ccb413bf05f5964ec) appears at position index 1 (0-based) in both files.
    # That's the one that should be in teacher-photo-wrap.

    # Strategy: the teacher photo is the one that appears at consistent position across files
    # and has md5=470ccb413bf05f5964ec
    MANABIKO_TEACHER_MD5 = "470ccb413bf05f5964ec"

    teacher_photo_idx = None
    for i, m in enumerate(matches):
        md5 = get_md5(m.group(4))
        if md5 == MANABIKO_TEACHER_MD5:
            teacher_photo_idx = i
            break

    return teacher_wrap_idx, teacher_photo_idx


def process_file(fpath: str) -> dict:
    is_englishroom = "englishroom" in fpath
    is_manabiko = "manabiko" in fpath

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    matches = list(IMG_WRAP_PATTERN.finditer(content))

    print(f"\n{'='*60}")
    print(f"File: {fpath.split('/')[-1]}")
    print(f"Found {len(matches)} img-wrap divs:")

    teacher_wrap_idx = None
    teacher_photo_idx = None

    for i, m in enumerate(matches):
        cls = m.group(2)
        b64 = m.group(4)
        md5 = get_md5(b64)
        size_kb = len(b64) * 3 / 4 / 1024
        is_teacher_wrap = "teacher-photo-wrap" in cls

        print(f"  [{i}] class={cls!r}, md5={md5[:20]}, size={size_kb:.0f}KB"
              + (" <-- teacher-photo-wrap" if is_teacher_wrap else ""))

        if is_teacher_wrap:
            teacher_wrap_idx = i

        if is_englishroom and md5.startswith(ENGLISHROOM_TEACHER_MD5_PREFIX):
            teacher_photo_idx = i
            print(f"       ^^^ TEACHER PHOTO (englishroom, md5 match)")

    if is_manabiko:
        teacher_wrap_idx, teacher_photo_idx = find_teacher_photo_index_manabiko(matches)
        if teacher_photo_idx is not None:
            print(f"  [{teacher_photo_idx}] identified as TEACHER PHOTO (manabiko, md5 match)")

    result = {
        "file": fpath,
        "matches_count": len(matches),
        "teacher_wrap_idx": teacher_wrap_idx,
        "teacher_photo_idx": teacher_photo_idx,
        "swapped": False,
        "error": None,
    }

    if teacher_wrap_idx is None:
        result["error"] = "No teacher-photo-wrap div found"
        print("  ERROR: No teacher-photo-wrap div found")
        return result

    if teacher_photo_idx is None:
        result["error"] = "Could not identify teacher photo"
        print("  ERROR: Could not identify teacher photo")
        return result

    if teacher_wrap_idx == teacher_photo_idx:
        print(f"  OK: Teacher photo is already in teacher-photo-wrap (index {teacher_wrap_idx})")
        return result

    # Need to swap the src values between teacher_wrap_idx and teacher_photo_idx
    print(f"\n  SWAP NEEDED: teacher photo at [{teacher_photo_idx}] but teacher-photo-wrap at [{teacher_wrap_idx}]")

    # Backup the file first
    backup_path = fpath + ".bak"
    shutil.copy2(fpath, backup_path)
    print(f"  Backup saved to: {backup_path.split('/')[-1]}")

    # Get the two match objects
    m_teacher_wrap = matches[teacher_wrap_idx]
    m_teacher_photo = matches[teacher_photo_idx]

    # We need to swap the `src` values (group(3) = full "data:image/...;base64,..." string)
    src_teacher_wrap = m_teacher_wrap.group(3)   # currently in teacher-photo-wrap (wrong)
    src_teacher_photo = m_teacher_photo.group(3) # actual teacher photo (wrong location)

    # We'll do the replacement carefully using positions in the string.
    # To avoid position shifts, replace from end to start.

    # Determine which comes first in the document
    pos_a = m_teacher_photo.start()
    pos_b = m_teacher_wrap.start()

    if pos_a < pos_b:
        first_match = m_teacher_photo
        first_new_src = src_teacher_wrap
        second_match = m_teacher_wrap
        second_new_src = src_teacher_photo
    else:
        first_match = m_teacher_wrap
        first_new_src = src_teacher_photo
        second_match = m_teacher_photo
        second_new_src = src_teacher_wrap

    # Find exact character positions of src attribute values within each match
    # group(3) is the full src value; group(0) is the full match text
    # We need the start of group(3) within group(0) to get absolute position in content

    def get_src_span(match):
        """Return (start, end) of the src value (group 3) in content."""
        match_start = match.start()
        match_text = match.group(0)
        # Find where group(3) starts within the match text
        src_val = match.group(3)
        offset_in_match = match_text.index(src_val)
        abs_start = match_start + offset_in_match
        abs_end = abs_start + len(src_val)
        return abs_start, abs_end

    # Replace from back to front to preserve positions
    s1, e1 = get_src_span(second_match)
    s2, e2 = get_src_span(first_match)

    # Verify
    assert content[s1:e1] == second_match.group(3), "Second match src verification failed"
    assert content[s2:e2] == first_match.group(3), "First match src verification failed"

    # Build new content: replace second first (higher position), then first
    new_content = content[:s1] + first_new_src + content[e1:]
    # Adjust second position: length might differ, so recalculate
    len_diff = len(first_new_src) - len(second_match.group(3))
    new_s2 = s2  # first_match comes before second_match, so s2 is unaffected
    new_e2 = e2
    new_content = new_content[:new_s2] + second_new_src + new_content[new_e2:]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    result["swapped"] = True
    print(f"  SWAPPED: src values exchanged between [{teacher_photo_idx}] and [{teacher_wrap_idx}]")
    print(f"  File saved: {fpath.split('/')[-1]}")

    return result


def verify_file(fpath: str):
    """Re-check the file after modification to confirm the fix."""
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    matches = list(IMG_WRAP_PATTERN.finditer(content))
    print(f"\n  Verification for {fpath.split('/')[-1]}:")
    for i, m in enumerate(matches):
        cls = m.group(2)
        b64 = m.group(4)
        md5 = get_md5(b64)
        size_kb = len(b64) * 3 / 4 / 1024
        is_teacher_wrap = "teacher-photo-wrap" in cls
        marker = " <-- teacher-photo-wrap" if is_teacher_wrap else ""
        print(f"    [{i}] md5={md5[:20]}, size={size_kb:.0f}KB{marker}")


def main():
    print("Teacher Photo Position Fix")
    print(f"Run at: {datetime.now().isoformat()}")

    results = []
    for fpath in FILES:
        result = process_file(fpath)
        results.append(result)

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    for r in results:
        fname = r["file"].split("/")[-1]
        if r["error"]:
            print(f"  {fname}: ERROR - {r['error']}")
        elif r["swapped"]:
            print(f"  {fname}: SWAPPED (teacher_photo_idx={r['teacher_photo_idx']} <-> teacher_wrap_idx={r['teacher_wrap_idx']})")
        else:
            print(f"  {fname}: OK (no swap needed)")

    # Verify swapped files
    swapped_files = [r["file"] for r in results if r["swapped"]]
    if swapped_files:
        print("\nPost-swap verification:")
        for fpath in swapped_files:
            verify_file(fpath)


if __name__ == "__main__":
    main()
