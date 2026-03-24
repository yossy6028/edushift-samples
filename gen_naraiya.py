#!/usr/bin/env python3
"""Generate naraiya-a.html and naraiya-b.html for ならいや 前田塾."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_school_html import generate_html

# ── Shared config fields ──
SHARED = {
    "name": "ならいや 前田塾",
    "subtitle": "三重県松阪市の個別指導塾",
    "title": "ならいや 前田塾｜三重県松阪市の個別指導・英会話",
    "meta_desc": "三重県松阪市の学習塾。小1から高3まで対応の個別指導講座、少人数クラス、英会話講座。定期テスト対策・入試対策・無料補習・自習スペース完備。2022年開校、地域密着の安心価格。",
    "logo_icon": "習",
    "img_dir": "naraiya",
    "original_url": "https://naraiya0326.wixsite.com/-site",

    # Hero
    "hero_badge": "小1~高3対応 / 個別指導・英会話",
    "hero_desc": "生徒一人ひとりの学力や性格に合わせたきめ細かな個別指導講座。教科書内容はもちろん、定期テスト対策から入試対策まで対応。さらに日々の学校の宿題などもサポートします。プロの講師陣が学習目標の達成をお約束いたします。また英会話講座では、受験英語だけでなく、リスニング力や将来役立つ英会話スキルが身につきます。",
    "hero_img_position": "center 30%",

    # CTA
    "cta_short": "無料体験はこちら",
    "cta_text": "無料体験授業に申し込む",
    "cta_title": "まずは無料体験授業から",
    "cta_desc": "お子さまに合った学び方を、実際の授業で体験してください。お気軽にお問い合わせください。",

    # Features (all original features preserved)
    "features_desc": "2022年3月開校。わからない生徒の気持ちにとことん寄り添い、一人ひとりの目標達成に向けて講師陣が一丸となって指導します。",
    "features": [
        {
            "title": "とことん寄り添う個別指導",
            "desc": "生徒一人ひとりの学力や性格に合わせたきめ細かな個別指導講座。教科書内容はもちろん、定期テスト対策から入試対策まで対応。さらに日々の学校の宿題などもサポートします。プロの講師陣が学習目標の達成をお約束いたします。",
        },
        {
            "title": "少人数クラスコース",
            "desc": "講師ひとりに対して生徒が10名ほどの少人数クラスコース。きめ細かな目配りが可能な環境で、集団の中でも一人ひとりに目が行き届く指導を実現しています。",
        },
        {
            "title": "小学生限定「ならいやクラブ」",
            "desc": "反復学習で小学校の算数と中学数学をスムーズに解くための計算力を徹底的に定着。国語では漢字の「読み」「書き」を大切にした基礎学力を徹底的に定着させます。小学生のうちにしっかりとした土台を築きます。",
        },
        {
            "title": "中3限定 高校受験コース（入試特訓講座）",
            "desc": "受験に特化した中3限定高校受験コース。高校入試を意識した応用力を養成する講座で、受験必勝を目指します。学習指導のみならず進路アドバイスもしっかり行い、志望校合格を目指します。毎年9月開講です。",
        },
        {
            "title": "英会話講座",
            "desc": "受験英語だけでなく、リスニング力や将来役立つ英会話スキルが身につきます。英会話講座のみ、高校生から大学生、社会人まで対応です。TOEICや英検にも挑戦できる実践的な英語力を養います。",
        },
        {
            "title": "無料補習・テスト対策・自習スペース完備",
            "desc": "無料補習に加え、定期テスト前には授業日以外にも無料のテスト対策を実施。質問可能な自習スペースも完備しており、いつでも学べる環境を整えています。通い放題の自習室で、自分のペースで学習を進められます。",
        },
        {
            "title": "地域密着の安心価格・兄弟割引あり",
            "desc": "地域密着の安心価格で通いやすい料金設定です。ご兄弟で通われる場合は兄弟割引もご利用いただけます。ご家庭の負担を軽減しながら、質の高い指導を提供します。",
        },
    ],

    # Courses
    "courses_desc": "小学1年生から高校3年生まで、一人ひとりの目標に合わせたコースをご用意しています。",
    "courses": [
        {
            "label": "小学生",
            "title": "ならいやクラブ（小学生限定）",
            "desc": "反復学習で算数の計算力と国語の漢字の「読み」「書き」を徹底定着。小学校の基礎学力をしっかり固め、中学へのスムーズな接続を目指します。",
        },
        {
            "label": "中学生",
            "title": "個別指導講座（中学生）",
            "desc": "教科書内容から定期テスト対策、入試対策まで幅広く対応。一人ひとりの学力や性格に合わせたきめ細かな指導で、学校の宿題もサポートします。",
        },
        {
            "label": "中3受験",
            "title": "入試特訓講座（中3限定・高校受験コース）",
            "desc": "高校入試を意識した応用力を養成。受験必勝を目指し、学習指導のみならず進路アドバイスもしっかり行います。毎年9月開講。志望校合格へ向けて徹底サポート。",
        },
        {
            "label": "高校生",
            "title": "個別指導講座（高校生）",
            "desc": "高校の教科書内容から大学受験対策まで対応。生徒一人ひとりの目標に合わせた個別カリキュラムで、効率的な学習をサポートします。",
        },
        {
            "label": "英会話",
            "title": "英会話講座",
            "desc": "受験英語だけでなく、リスニング力や将来役立つ英会話スキルが身につきます。高校生から大学生、社会人まで対応。TOEICや英検にも対応した実践的な英語力を養います。",
        },
    ],
    "default_course_index": 1,

    # FAQ
    "faq": [
        ("対象学年は何年生からですか？", "個別指導講座は小学1年生から高校3年生まで対応しています。英会話講座は高校生から社会人まで受講可能です。小学生限定の「ならいやクラブ」もございます。"),
        ("無料体験授業はありますか？", "はい、無料体験授業を随時受け付けております。実際の授業を体験していただき、お子さまに合った学び方をご確認ください。"),
        ("兄弟割引はありますか？", "はい、ご兄弟で通われる場合は兄弟割引をご利用いただけます。詳しくはお問い合わせください。"),
        ("自習室は使えますか？", "はい、通い放題の自習室を完備しています。質問可能な自習スペースですので、授業日以外でもご利用いただけます。"),
        ("定期テスト対策はありますか？", "はい、定期テスト前には授業日以外にも無料のテスト対策を実施しています。無料補習もございます。"),
        ("入試対策はしてもらえますか？", "はい、中3限定の入試特訓講座（毎年9月開講）のほか、個別指導講座でも入試対策に対応しています。進路アドバイスもしっかり行います。"),
        ("2校目があると聞きましたが？", "はい、2024年に移転し、2025年には2校目（明和校）を開校いたしました。より多くの生徒さまにご利用いただける体制を整えています。"),
    ],

    # Access
    "address": "三重県松阪市大黒田町479-1",
    "access_items": [
        {"icon": "所", "label": "所在地（松阪校）", "value": "〒515-0063 三重県松阪市大黒田町479-1"},
        {"icon": "電", "label": "電話番号", "value": '<a href="tel:0598-31-3120" style="color:inherit">0598-31-3120</a>'},
        {"icon": "時", "label": "お問い合わせ", "value": "お電話またはホームページよりお気軽にどうぞ"},
        {"icon": "駅", "label": "最寄り", "value": "小春区徒歩10秒"},
    ],

    # Footer
    "footer_desc": "2022年3月開校。三重県松阪市で小1から高3まで対応の学習塾。個別指導・少人数クラス・英会話講座で、一人ひとりの目標達成を全力サポートします。",

    # Instructor / narrative section
    "instructor": {
        "title": "ならいや 前田塾のこだわり",
        "label": "OUR BELIEF",
        "content": """<p>私たちは「わからない」という気持ちに、とことん寄り添います。</p>
<p>勉強が苦手な子、なかなか成績が上がらない子。そんな生徒たちの「わからない」には、必ず理由があります。私たちはその理由を一緒に見つけ、一つひとつ丁寧に解きほぐしていきます。</p>
<p>2022年3月に松阪市で開校して以来、地域のお子さまたちの学びを支え続けてきました。小学1年生から高校3年生まで、一人ひとりの学力や性格に合わせたきめ細かな指導を大切にしています。</p>
<p>教科書の内容はもちろん、定期テスト対策から入試対策、日々の宿題サポートまで。プロの講師陣が学習目標の達成をお約束します。無料補習やテスト前の無料対策、通い放題の自習室など、いつでも学べる環境を整えています。</p>
<p>2024年の移転、2025年の明和校開校と、より多くの生徒さまに寄り添える体制を築いてまいりました。地域密着の安心価格と兄弟割引で、ご家庭に寄り添いながら質の高い指導をお届けします。</p>
<p><span class="belief-accent">わからない気持ちを、わかる喜びへ。</span>それが、ならいや前田塾の信念です。</p>""",
    },

    # Improvement points
    "improvement_points": [
        {
            "title": "スマートフォン対応の最適化",
            "before": "元HPはWixで構築されており、モバイル表示時にレイアウトの崩れや読み込み速度の低下が見られます。保護者がスマートフォンで閲覧する機会が多い中、操作性に課題があります。",
            "after": "レスポンシブデザインを採用し、スマートフォンでも快適に閲覧できるよう最適化。ページ読み込み速度も大幅に改善し、保護者のストレスを軽減します。",
        },
        {
            "title": "コース・料金情報の構造化",
            "before": "元HPではコース情報が分散しており、小学生・中学生・高校生・英会話の各コース詳細や料金体系がひと目で比較しにくい構成になっています。",
            "after": "タブ切替式のコース紹介で、学年別のコース内容を直感的に比較可能に。保護者が求める情報にすぐたどり着ける導線を設計しました。",
        },
        {
            "title": "塾の信念・差別化ポイントの訴求強化",
            "before": "元HPでは塾の特徴や想いが複数ページに分散しており、初見の保護者に対して「この塾を選ぶ理由」が十分に伝わりにくい構成です。",
            "after": "ナラティブ形式の「こだわりセクション」で塾長の想いを一箇所に集約。7つの特長を視覚的に整理し、他塾との差別化ポイントを明確に打ち出しました。",
        },
    ],
}

# ── A pattern config: bright orange, friendly font, story-type hero ──
config_a = {
    **SHARED,
    "primary": "#E65100",
    "primary_light": "#FF8A65",
    "navy": "#1A1A2E",
    "bg_warm": "#FFF8F0",
    "cta_gradient_start": "#BF360C",
    "font_preset": "friendly",
    "hero_h1": '<em>とことん寄り添う</em><br>一人ひとりの目標達成へ',
    "hero_stats": [
        {"num": "2022", "label": "年開校"},
        {"num": "小1~高3", "label": "全学年対応"},
        {"num": "2", "label": "校（松阪・明和）"},
    ],
}

# ── B pattern config: dark brown, classic font (明朝体), stats-type hero ──
config_b = {
    **SHARED,
    "primary": "#4E342E",
    "primary_light": "#8D6E63",
    "navy": "#212121",
    "bg_warm": "#F5F0EB",
    "cta_gradient_start": "#3E2723",
    "font_preset": "classic",
    "hero_h1": '<em>わからないを、わかるへ</em><br>松阪市の個別指導塾',
    "hero_stats": [
        {"num": "小1~高3", "label": "全学年対応"},
        {"num": "5", "label": "コース展開"},
        {"num": "2", "label": "校舎（松阪・明和）"},
    ],
}

# ── Generate ──
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
for suffix, cfg in [("a", config_a), ("b", config_b)]:
    html = generate_html(cfg)
    path = os.path.join(OUT_DIR, f"naraiya-{suffix}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {path}")

# ── Quality checks ──
import re
for suffix in ("a", "b"):
    path = os.path.join(OUT_DIR, f"naraiya-{suffix}.html")
    with open(path) as f:
        html = f.read()
    checks = {
        "R1_single_file": True,
        "R2_viewport": "viewport" in html,
        "R4_IntersectionObserver": "IntersectionObserver" in html,
        "R5_floating_CTA": "floating" in html.lower(),
        "R6_hamburger": "hamburger" in html,
        "R7_imgs_3plus": len(re.findall(r'data:image/jpeg;base64,', html)) >= 3,
        "R16_base64_embedded": len(re.findall(r'data:image/jpeg;base64,', html)) >= 3,
        "R17_gmap": "maps.google.com" in html,
        "R18_overlay": "img-overlay" in html,
        "R20_no_emoji": len(re.findall('[\U0001F300-\U0001FAFF\U00002600-\U000027BF]', html)) == 0,
        "R21_js_fallback": "setTimeout" in html,
        "R22_no_placeholder": "公式サイトでご確認ください" not in html,
    }
    fails = [k for k, v in checks.items() if not v]
    status = "ALL PASS" if not fails else "FAIL: " + ", ".join(fails)
    print(f"naraiya-{suffix}.html: {status}")
