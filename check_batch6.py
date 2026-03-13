#!/usr/bin/env python3
"""
PJ1 Batch6 品質チェックスクリプト
対象: izumi-a/b, uji-a/b, em-a/b, expert-a/b, miyuki-a/b, yume-a/b, keio-a/b, kishiwada-a/b
"""

import os
import re
import hashlib
import sys

BASE_DIR = "/Users/yossy/edushift-samples"

TARGET_FILES = [
    "izumi-a.html", "izumi-b.html",
    "uji-a.html", "uji-b.html",
    "em-a.html", "em-b.html",
    "expert-a.html", "expert-b.html",
    "miyuki-a.html", "miyuki-b.html",
    "yume-a.html", "yume-b.html",
    "keio-a.html", "keio-b.html",
    "kishiwada-a.html", "kishiwada-b.html",
]

# Unicode絵文字の範囲（CJK文字を除外した正確なパターン）
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002702-\U000027B0"  # dingbats
    "\U00002300-\U000023FF"  # misc technical
    "]+",
    flags=re.UNICODE
)


def check_file(filepath):
    results = {}
    filename = os.path.basename(filepath)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return {"ERROR": str(e)}

    filesize = os.path.getsize(filepath)

    # R2: viewport meta定義あり
    results["R2_viewport"] = "PASS" if '<meta name="viewport"' in content or "<meta name='viewport'" in content else "FAIL"

    # R4: IntersectionObserver使用
    results["R4_intersection_observer"] = "PASS" if "IntersectionObserver" in content else "FAIL"

    # R5: floating CTA
    results["R5_floating_cta"] = "PASS" if "floating-line" in content or "floating-cta" in content else "FAIL"

    # R6: ハンバーガーメニュー
    results["R6_hamburger"] = "PASS" if "hamburger" in content or "ham-menu" in content else "FAIL"

    # R7/R16: base64画像3枚以上
    base64_count = content.count("data:image/")
    results["R7_R16_base64_images"] = "PASS" if base64_count >= 3 else f"FAIL (count={base64_count})"

    # R17: Google Map埋め込み
    has_map = (
        "maps.google" in content
        or "google.com/maps" in content
        or ("iframe" in content.lower() and "map" in content.lower())
    )
    results["R17_google_map"] = "PASS" if has_map else "FAIL"

    # R18: img-overlay（差替え可能 or img-overlay）
    results["R18_img_overlay"] = "PASS" if "差替え可能" in content or "img-overlay" in content else "FAIL"

    # R20: 絵文字なし（CJK文字を除外した正確なパターンで検出）
    emoji_matches = EMOJI_PATTERN.findall(content)
    if emoji_matches:
        results["R20_no_emoji"] = f"FAIL (found: {emoji_matches[:5]})"
    else:
        results["R20_no_emoji"] = "PASS"

    # R21: setTimeout
    results["R21_set_timeout"] = "PASS" if "setTimeout" in content else "FAIL"

    # R22: プレースホルダ文言なし
    results["R22_no_placeholder"] = "PASS" if "公式サイトでご確認ください" not in content else "FAIL"

    # R24: 同一画像の重複使用なし（フルbase64文字列でハッシュ比較）
    base64_strings = re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]{100,})', content)
    if base64_strings:
        hashes = [hashlib.md5(s.encode()).hexdigest() for s in base64_strings]
        from collections import Counter
        dup_hashes = [h for h, cnt in Counter(hashes).items() if cnt > 1]
        if dup_hashes:
            results["R24_no_duplicate_images"] = f"FAIL (duplicates found: {len(dup_hashes)} groups)"
        else:
            results["R24_no_duplicate_images"] = "PASS"
    else:
        results["R24_no_duplicate_images"] = "PASS (no base64)"

    # R25: aspect-ratio 16/9 なし
    has_16_9 = bool(re.search(r'aspect-ratio\s*:\s*16\s*/\s*9', content))
    results["R25_no_aspect_16_9"] = "PASS" if not has_16_9 else "FAIL"

    # R26: object-fit: cover あり
    has_cover = bool(re.search(r'object-fit\s*:\s*cover', content))
    results["R26_object_fit_cover"] = "PASS" if has_cover else "FAIL"

    # R33: hero-photo-badge要素なし
    results["R33_no_hero_photo_badge"] = "PASS" if "hero-photo-badge" not in content else "FAIL"

    # R34: EduShift提案セクションがfooter後にある
    footer_match = re.search(r'</footer>', content, re.IGNORECASE)
    if footer_match:
        after_footer = content[footer_match.end():]
        # EduShift提案セクションの識別: コメント・URL・POWERED BY EDUSHIFT等
        has_edushift_after = (
            "EduShift" in after_footer
            or "EDUSHIFT" in after_footer
            or "edu-shift-cta" in after_footer
            or "edushift-proposal" in after_footer
            or "edu-shift.com" in after_footer
            or "POWERED BY EDUSHIFT" in after_footer
        )
        if has_edushift_after:
            results["R34_edushift_after_footer"] = "PASS"
        else:
            # footer前に存在するか確認
            before_footer = content[:footer_match.start()]
            has_before = (
                "edu-shift-cta" in before_footer
                or "edushift-proposal" in before_footer
                or "POWERED BY EDUSHIFT" in before_footer
            )
            if has_before:
                results["R34_edushift_after_footer"] = "FAIL (section is before/inside footer)"
            else:
                results["R34_edushift_after_footer"] = "FAIL (section not found)"
    else:
        has_section = "edu-shift-cta" in content or "edushift-proposal" in content
        results["R34_edushift_after_footer"] = "FAIL (no </footer> tag)" if has_section else "FAIL (section not found, no footer)"

    # CSS変数: --primary と --accent が :root に定義
    root_match = re.search(r':root\s*\{([^}]+)\}', content)
    if root_match:
        root_content = root_match.group(1)
        has_primary = "--primary" in root_content
        has_accent = "--accent" in root_content
        if has_primary and has_accent:
            results["CSS_variables"] = "PASS"
        else:
            missing = []
            if not has_primary:
                missing.append("--primary")
            if not has_accent:
                missing.append("--accent")
            results["CSS_variables"] = f"FAIL (missing: {', '.join(missing)})"
    else:
        results["CSS_variables"] = "FAIL (no :root found)"

    # EduShift URL
    correct_url = "https://www.edu-shift.com/service/hp-production"
    results["EduShift_URL"] = "PASS" if correct_url in content else "FAIL"

    # ファイルサイズ: 200KB以上
    size_kb = filesize / 1024
    results["FileSize_200KB"] = "PASS" if filesize >= 200 * 1024 else f"FAIL ({size_kb:.1f}KB)"

    return results


def main():
    all_results = {}

    print("=" * 80)
    print("PJ1 Batch6 品質チェック結果")
    print("=" * 80)

    # 全チェック項目キーリスト
    check_keys = [
        "R2_viewport", "R4_intersection_observer", "R5_floating_cta",
        "R6_hamburger", "R7_R16_base64_images", "R17_google_map",
        "R18_img_overlay", "R20_no_emoji", "R21_set_timeout",
        "R22_no_placeholder", "R24_no_duplicate_images", "R25_no_aspect_16_9",
        "R26_object_fit_cover", "R33_no_hero_photo_badge",
        "R34_edushift_after_footer", "CSS_variables", "EduShift_URL",
        "FileSize_200KB"
    ]

    for filename in TARGET_FILES:
        filepath = os.path.join(BASE_DIR, filename)
        results = check_file(filepath)
        all_results[filename] = results

        print(f"\n{'─' * 60}")
        print(f"FILE: {filename}")
        print(f"{'─' * 60}")

        fail_items = []
        for key in check_keys:
            status = results.get(key, "N/A")
            mark = "✓" if status == "PASS" else "✗"
            print(f"  {mark} {key}: {status}")
            if status != "PASS":
                fail_items.append(key)

        if fail_items:
            print(f"\n  *** FAIL items: {', '.join(fail_items)} ***")
        else:
            print("\n  *** ALL PASS ***")

    # サマリー
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    total_fails = 0
    for filename in TARGET_FILES:
        results = all_results[filename]
        fails = [k for k in check_keys if results.get(k, "N/A") != "PASS"]
        total_fails += len(fails)
        status_str = "ALL PASS" if not fails else f"FAIL ({len(fails)} items)"
        print(f"  {filename:<25} {status_str}")
        for f in fails:
            print(f"    - {f}: {results.get(f)}")

    print(f"\nTotal FAIL items across all files: {total_fails}")
    print("=" * 80)

    return all_results


if __name__ == "__main__":
    main()
