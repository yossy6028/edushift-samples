import re
import os

def process_file(filepath, is_englishroom):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the teacher-photo-wrap div and extract the img tag inside it
    marker = 'class="img-wrap teacher-photo-wrap"'
    pos = content.find(marker)
    if pos == -1:
        print(f"WARNING: teacher-photo-wrap not found in {filepath}")
        return

    # Find the start of this div
    div_start = content.rfind('<div', 0, pos)

    # Find the closing </div> of this div by counting nested divs
    search_from = div_start + 4
    depth = 1
    close_pos = search_from
    while depth > 0:
        next_open = content.find('<div', search_from)
        next_close = content.find('</div>', search_from)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            search_from = next_open + 4
        else:
            depth -= 1
            close_pos = next_close
            search_from = next_close + 6

    div_end = close_pos + 6  # len('</div>') = 6

    # Extract the full div content
    teacher_div_content = content[div_start:div_end]

    # Extract the img tag from within
    img_start = teacher_div_content.find('<img ')
    img_end = teacher_div_content.find('>', img_start) + 1
    teacher_img = teacher_div_content[img_start:img_end]

    print(f"  Extracted img tag length: {len(teacher_img)} chars")

    # Step 2: Replace in zigzag - change class to just "img-wrap"
    new_zigzag_div = teacher_div_content.replace('class="img-wrap teacher-photo-wrap"', 'class="img-wrap"', 1)
    content = content[:div_start] + new_zigzag_div + content[div_end:]

    # Step 3: Build new teacher section
    if is_englishroom:
        teacher_section = f'''
<section id="teacher" style="padding:64px 5vw;background:var(--bg-alt,#f7f7f7);">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <h2 class="section-title">講師紹介</h2>
    <div class="section-divider"></div>
    <div class="teacher-photo-wrap">
      <!-- 元HPより: 講師のお写真 -->
      {teacher_img}
    </div>
    <h3 style="font-size:1.3rem;margin:1rem 0 0.5rem;">Mina先生</h3>
    <p style="font-size:1rem;color:var(--text-sub);line-height:1.8;text-align:left;max-width:700px;margin:0 auto;">
      アメリカ在住歴17年、大手子ども英会話教室で8年間教えてきた経験豊富な講師です。これまで約200名の生徒を指導してきました。大型教室では生徒一人ひとりのニーズに応えきれないと感じ、個人教室を開きました。
    </p>
    <div style="text-align:left;max-width:700px;margin:1.5rem auto 0;">
      <h4 style="font-size:1.1rem;margin-bottom:0.8rem;">English Roomが選ばれる理由</h4>
      <ul style="list-style:none;padding:0;">
        <li style="padding:12px 0;border-bottom:1px solid #eee;"><strong>レベル別クラス</strong><br>お子様の年齢ではなく、一人ひとりのレベルに合わせてクラスをご提案します。</li>
        <li style="padding:12px 0;border-bottom:1px solid #eee;"><strong>少人数制（1〜5人）</strong><br>先生の目が一人ひとりに届き、発言機会が多く、確実に会話力が伸びる環境です。</li>
        <li style="padding:12px 0;border-bottom:1px solid #eee;"><strong>経験豊富な日本人講師</strong><br>外国人講師が苦手なお子様も安心。丁寧でわかりやすい指導を行います。</li>
        <li style="padding:12px 0;"><strong>振替レッスン対応</strong><br>欠席時も年度末まで振替レッスンが可能。お月謝を無駄にしません。</li>
      </ul>
    </div>
  </div>
</section>

'''
    else:  # manabiko
        teacher_section = f'''
<section id="teacher" style="padding:64px 5vw;background:var(--bg-alt,#f7f7f7);">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <h2 class="section-title">講師紹介</h2>
    <div class="section-divider"></div>
    <div class="teacher-photo-wrap">
      <!-- 元HPより: 講師のお写真 -->
      {teacher_img}
    </div>
    <h3 style="font-size:1.3rem;margin:1rem 0 0.5rem;">橋口先生</h3>
    <p style="font-size:1rem;color:var(--text-sub);line-height:1.8;text-align:left;max-width:700px;margin:0 auto;">
      中学生から高校2年生までを対象に、英語が苦手な生徒でも安心して学べる環境を提供しています。1対1のオンラインレッスンで、一人ひとりに合わせた指導を行います。独自教材で基礎力を固め、定期テストや英検対策（5級〜準1級）にも対応しています。
    </p>
    <div style="text-align:left;max-width:700px;margin:1.5rem auto 0;">
      <h4 style="font-size:1.1rem;margin-bottom:0.8rem;">この教室ならではの特長</h4>
      <ul style="list-style:none;padding:0;">
        <li style="padding:12px 0;border-bottom:1px solid #eee;"><strong>1対1のオンラインレッスン</strong><br>ご自宅から安心してご受講いただけます。</li>
        <li style="padding:12px 0;border-bottom:1px solid #eee;"><strong>基礎を大切にした指導</strong><br>基礎力を身につけるためのワークブックを使用し、英語を基礎から丁寧に指導します。</li>
        <li style="padding:12px 0;"><strong>英検5級〜準1級まで対応</strong><br>一次試験・二次試験（面接）対策、英作文の添削指導も行っています。</li>
      </ul>
    </div>
  </div>
</section>

'''

    # Step 4: Insert before price section
    price_marker = '<section class="price-section" id="price">'
    price_pos = content.find(price_marker)
    if price_pos == -1:
        print(f"WARNING: price section not found in {filepath}")
        return

    content = content[:price_pos] + teacher_section + content[price_pos:]

    # Write output
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Done: {filepath}")


# Process all files
base = '/Users/yossy/edushift-samples'

files = [
    ('englishroom-a.html', True),
    ('englishroom-b.html', True),
    ('manabiko-a.html', False),
    ('manabiko-b.html', False),
]

for filename, is_englishroom in files:
    filepath = os.path.join(base, filename)
    print(f"\nProcessing: {filename}")

    # Create backup
    backup = filepath + '.bak2'
    if not os.path.exists(backup):
        with open(filepath, 'rb') as f:
            data = f.read()
        with open(backup, 'wb') as f:
            f.write(data)
        print(f"  Backup created: {backup}")
    else:
        print(f"  Backup already exists: {backup}")

    process_file(filepath, is_englishroom)

print("\nAll files processed.")
