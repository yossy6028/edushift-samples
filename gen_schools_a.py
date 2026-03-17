#!/usr/bin/env python3
# gen_schools_a.py — Generate A-variant HTML files for 5 Japanese cram schools

import os

IMG_DIR = "/Users/yossy/.openclaw/workspace-nanami/projects/pj1/images/library/b64"
OUT_DIR = "/Users/yossy/edushift-samples"

IMAGE_NAMES = [
    "classroom_exam-schedule-01",       # 0
    "classroom_reception-achievement-01",# 1
    "classroom_study-corner-01",        # 2
    "classroom_waiting-area-01",        # 3
    "exam_stationery-01",               # 4
    "hero_individual-tutor-01",         # 5
    "hero_modern-study-01",             # 6
    "hero_partitioned-desk-01",         # 7
    "hero_self-study-01",               # 8
    "hero_test-prep-01",                # 9
    "hero_warm-entrance-01",            # 10
    "study_compact-partitioned-01",     # 11
    "study_desk-closeup-01",            # 12
    "study_math-help-01",               # 13
    "study_row-desks-01",               # 14
    "study_rural-tutor-01",             # 15
    "study_small-group-01",             # 16
    "study_stationery-01",              # 17
    "study_tutor-elementary-01",        # 18
    "support_tools-01",                 # 19
]

def read_img(name):
    path = os.path.join(IMG_DIR, name + ".b64")
    with open(path, "r") as f:
        content = f.read().strip()
    return "data:image/jpeg;base64," + content

def img_tag(data_uri, alt=""):
    return f'<img src="{data_uri}" alt="{alt}" loading="lazy">'

def img_wrap(data_uri, alt=""):
    overlay_text = "写真はサンプルです。ご希望に応じて変更可能です。"
    return f'''<div class="img-wrap">
  {img_tag(data_uri, alt)}
  <div class="img-overlay">{overlay_text}</div>
</div>'''

COMMON_CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;overflow-x:hidden;}
body{font-family:'Noto Sans JP',sans-serif;color:var(--text);background:var(--white);overflow-x:hidden;}
a{text-decoration:none;color:inherit;}
img{max-width:100%;height:auto;display:block;}

/* === FADE ANIMATIONS === */
.fade-in{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade-left{opacity:0;transform:translateX(-40px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade-right{opacity:0;transform:translateX(40px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade-in.visible,.fade-left.visible,.fade-right.visible{opacity:1;transform:none;}

/* === HEADER === */
.site-header{position:sticky;top:0;z-index:100;background:var(--navy);box-shadow:0 2px 12px rgba(0,0,0,0.18);}
.header-inner{max-width:1100px;margin:0 auto;padding:0 24px;height:64px;display:flex;align-items:center;justify-content:space-between;}
.logo{font-family:'Noto Serif JP',serif;font-size:1.15rem;font-weight:700;color:var(--white);letter-spacing:0.04em;}
.pc-nav{display:flex;align-items:center;gap:20px;}
.pc-nav a{color:var(--white);font-size:0.88rem;font-weight:500;opacity:0.9;transition:opacity 0.2s;}
.pc-nav a:hover{opacity:1;}
.nav-cta{background:var(--gold);color:var(--navy-dark)!important;padding:8px 20px;border-radius:24px;font-weight:700!important;font-size:0.85rem!important;opacity:1!important;transition:background 0.2s!important;}
.nav-cta:hover{background:var(--gold-light)!important;}
.hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px;}
.hamburger span{display:block;width:24px;height:2px;background:var(--white);transition:transform 0.3s,opacity 0.3s;}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
.hamburger.open span:nth-child(2){opacity:0;}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}

/* === MOBILE NAV === */
#mobile-nav{display:none;position:fixed;top:64px;left:0;width:100%;background:var(--navy-dark);z-index:99;padding:16px 0;}
#mobile-nav.open{display:block;}
.mobile-link{display:block;color:var(--white);padding:14px 28px;font-size:0.95rem;border-bottom:1px solid rgba(255,255,255,0.08);}
.mobile-link:last-child{border-bottom:none;}

/* === HERO === */
.hero{position:relative;min-height:520px;display:flex;align-items:center;overflow:hidden;}
.hero-bg{position:absolute;inset:0;z-index:0;}
.hero-bg img{width:100%;height:100%;object-fit:cover;object-position:center;}
.hero-bg::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,36,64,0.82) 0%,rgba(15,36,64,0.45) 60%,rgba(15,36,64,0.2) 100%);}
.hero-overlay-text{position:absolute;bottom:0;left:0;background:rgba(0,0,0,0.55);color:#fff;font-size:0.7rem;padding:2px 8px;width:100%;box-sizing:border-box;text-align:center;pointer-events:none;z-index:2;}
.hero-content{position:relative;z-index:3;max-width:1100px;margin:0 auto;padding:80px 40px;}
.hero-tag{display:inline-block;background:var(--gold);color:var(--navy-dark);font-size:0.78rem;font-weight:700;padding:4px 14px;border-radius:2px;letter-spacing:0.08em;margin-bottom:18px;}
.hero h1{font-family:'Noto Serif JP',serif;font-size:clamp(1.7rem,4vw,2.8rem);font-weight:700;color:var(--white);line-height:1.4;margin-bottom:20px;}
.hero h1 span{color:var(--gold);}
.hero-sub{color:rgba(255,255,255,0.88);font-size:0.95rem;line-height:1.8;max-width:520px;margin-bottom:32px;}
.hero-btns{display:flex;gap:14px;flex-wrap:wrap;}
.btn-primary{background:var(--gold);color:var(--navy-dark);padding:14px 32px;border-radius:4px;font-weight:700;font-size:0.95rem;transition:background 0.2s,transform 0.2s;display:inline-block;}
.btn-primary:hover{background:var(--gold-light);transform:translateY(-2px);}
.btn-outline{background:transparent;color:var(--white);border:2px solid rgba(255,255,255,0.7);padding:12px 28px;border-radius:4px;font-weight:500;font-size:0.95rem;transition:border-color 0.2s,background 0.2s;display:inline-block;}
.btn-outline:hover{border-color:var(--white);background:rgba(255,255,255,0.1);}

/* === SECTION COMMON === */
.section{padding:80px 0;}
.section-inner{max-width:1100px;margin:0 auto;padding:0 40px;}
.section-label{font-size:0.72rem;font-weight:700;letter-spacing:0.18em;color:var(--gold);text-transform:uppercase;margin-bottom:8px;}
.section-title{font-family:'Noto Serif JP',serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:700;color:var(--navy);margin-bottom:40px;line-height:1.4;}
.section-title span{color:var(--gold);}

/* === FEATURES === */
.features{background:var(--warm-white);}
.features-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:40px;}
.feature-card{background:var(--white);border-radius:8px;padding:32px 24px;text-align:center;box-shadow:0 4px 20px rgba(26,58,92,0.07);border-top:4px solid var(--gold);}
.feature-icon{width:52px;height:52px;margin:0 auto 18px;display:flex;align-items:center;justify-content:center;}
.icon-star{position:relative;width:40px;height:40px;}
.icon-star::before,.icon-star::after{content:'';position:absolute;inset:0;background:var(--gold);clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);}
.icon-circle{width:40px;height:40px;border-radius:50%;background:var(--gold);margin:0 auto;}
.icon-diamond{width:32px;height:32px;background:var(--gold);transform:rotate(45deg);margin:4px auto;}
.icon-check{width:40px;height:40px;border:3px solid var(--gold);border-radius:50%;position:relative;}
.icon-check::after{content:'';position:absolute;left:9px;top:5px;width:12px;height:18px;border-right:3px solid var(--gold);border-bottom:3px solid var(--gold);transform:rotate(40deg);}
.icon-book{width:36px;height:40px;background:var(--navy);border-radius:2px 6px 6px 2px;position:relative;margin:0 auto;}
.icon-book::before{content:'';position:absolute;left:4px;top:6px;right:6px;height:2px;background:var(--gold);}
.icon-book::after{content:'';position:absolute;left:4px;top:12px;right:10px;height:2px;background:var(--gold);}
.icon-bolt{width:0;height:0;border-left:14px solid transparent;border-right:10px solid transparent;border-bottom:36px solid var(--gold);position:relative;margin:2px auto 0;}
.feature-card h3{font-weight:700;font-size:1rem;color:var(--navy);margin-bottom:10px;}
.feature-card p{font-size:0.85rem;color:var(--gray);line-height:1.7;}

/* === ZIGZAG === */
.zigzag{background:var(--white);}
.zz-row{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:0;border-bottom:1px solid var(--gray-light);}
.zz-row:last-child{border-bottom:none;}
.zz-row.reverse .zz-img{order:2;}
.zz-row.reverse .zz-text{order:1;}
.zz-img{aspect-ratio:4/3;overflow:hidden;position:relative;}
.zz-img img{width:100%;height:100%;object-fit:cover;transition:transform 0.5s ease;}
.zz-img:hover img{transform:scale(1.03);}
.zz-img .img-overlay{position:absolute;bottom:0;left:0;background:rgba(0,0,0,0.55);color:#fff;font-size:0.7rem;padding:2px 8px;width:100%;box-sizing:border-box;text-align:center;pointer-events:none;}
.zz-text{padding:48px 56px;}
.zz-text .zz-label{font-size:0.7rem;font-weight:700;letter-spacing:0.18em;color:var(--gold);text-transform:uppercase;margin-bottom:10px;}
.zz-text h3{font-family:'Noto Serif JP',serif;font-size:1.35rem;font-weight:700;color:var(--navy);margin-bottom:16px;line-height:1.5;}
.zz-text p{font-size:0.9rem;color:var(--gray);line-height:1.8;}

/* === RESULTS === */
.results{background:var(--navy);}
.results .section-title{color:var(--white);}
.results .section-label{color:var(--gold-light);}
.results-year{color:var(--gold);font-size:0.88rem;font-weight:700;margin-bottom:28px;}
.results-groups{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;}
.results-group{background:rgba(255,255,255,0.07);border-radius:8px;padding:24px;}
.results-group h4{color:var(--gold);font-size:0.82rem;font-weight:700;letter-spacing:0.1em;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid rgba(200,168,60,0.3);}
.results-group ul{list-style:none;}
.results-group li{color:rgba(255,255,255,0.88);font-size:0.88rem;padding:4px 0;padding-left:14px;position:relative;}
.results-group li::before{content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);width:6px;height:6px;border-radius:50%;background:var(--gold);}

/* === TEACHER === */
.teacher{background:var(--warm-white);}
.teacher-inner{display:grid;grid-template-columns:auto 1fr;gap:60px;align-items:start;}
.teacher-photo-wrap{width:200px;height:200px;border-radius:50%!important;overflow:hidden;border:4px solid var(--gold);box-shadow:0 8px 32px rgba(26,58,92,0.15);margin:0 auto 24px;}
.teacher-photo-wrap .img-wrap{width:100%;height:100%;}
.teacher-photo-wrap .img-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.teacher-photo-col{text-align:center;}
.teacher-name{font-family:'Noto Serif JP',serif;font-size:1.3rem;font-weight:700;color:var(--navy);}
.teacher-title{font-size:0.82rem;color:var(--gold);font-weight:700;margin-top:4px;}
.teacher-text{font-size:0.92rem;line-height:1.85;color:var(--gray);margin-bottom:24px;}
.teacher-profile{list-style:none;display:flex;flex-direction:column;gap:8px;}
.teacher-profile li{font-size:0.85rem;color:var(--navy);padding-left:18px;position:relative;font-weight:500;}
.teacher-profile li::before{content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);width:8px;height:8px;background:var(--gold);border-radius:50%;}

/* === COURSES === */
.courses{background:var(--white);}
.courses-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:20px;}
.course-card{border:2px solid var(--gray-light);border-radius:8px;padding:28px 22px;transition:border-color 0.2s,box-shadow 0.2s;}
.course-card:hover{border-color:var(--gold);box-shadow:0 4px 20px rgba(200,168,60,0.15);}
.course-card h4{font-family:'Noto Serif JP',serif;font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:8px;}
.course-price{color:var(--gold-dark);font-size:1.1rem;font-weight:700;margin-bottom:12px;}
.course-card p{font-size:0.83rem;color:var(--gray);line-height:1.7;}
.courses-note{font-size:0.82rem;color:var(--gray);background:var(--warm-white);padding:14px 18px;border-radius:4px;border-left:3px solid var(--gold);}

/* === PRICE === */
.price{background:var(--warm-white);}
table{width:100%;border-collapse:collapse;}
table th,table td{padding:12px 16px;text-align:center;border:1px solid var(--gray-light);font-size:0.88rem;}
table th{background:var(--navy);color:var(--white);font-weight:700;}
table tr:nth-child(even) td{background:rgba(26,58,92,0.04);}
table td:first-child{font-weight:700;color:var(--navy);}
.price-notes{margin-top:14px;display:flex;flex-wrap:wrap;gap:10px;}
.price-note-item{font-size:0.8rem;color:var(--gray);background:var(--white);padding:6px 14px;border-radius:20px;border:1px solid var(--gray-light);}

/* === FLOW === */
.flow{background:var(--white);}
.flow-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:0;position:relative;margin-top:40px;}
.flow-steps::before{content:'';position:absolute;top:32px;left:10%;right:10%;height:2px;background:linear-gradient(90deg,var(--gold),var(--gold-light));z-index:0;}
.flow-step{position:relative;z-index:1;text-align:center;padding:0 12px;}
.step-num{width:64px;height:64px;border-radius:50%;background:var(--navy);color:var(--white);display:flex;align-items:center;justify-content:center;font-family:'Noto Serif JP',serif;font-size:1.3rem;font-weight:700;margin:0 auto 16px;border:3px solid var(--gold);}
.flow-step h4{font-size:0.92rem;font-weight:700;color:var(--navy);margin-bottom:8px;}
.flow-step p{font-size:0.8rem;color:var(--gray);line-height:1.6;}

/* === ACCESS === */
.access{background:var(--warm-white);}
.access-inner{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;}
.map-wrap{border-radius:8px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.1);}
.map-wrap iframe{width:100%;height:340px;border:none;display:block;}
.access-info h4{font-family:'Noto Serif JP',serif;font-size:1.2rem;font-weight:700;color:var(--navy);margin-bottom:24px;}
.access-item{display:flex;gap:14px;margin-bottom:18px;align-items:flex-start;}
.access-icon{width:32px;height:32px;border-radius:50%;background:var(--navy);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;}
.access-icon-inner{width:14px;height:14px;background:var(--gold);border-radius:50%;}
.access-label{font-size:0.75rem;color:var(--gold);font-weight:700;letter-spacing:0.1em;margin-bottom:3px;}
.access-val{font-size:0.9rem;color:var(--navy);line-height:1.6;}

/* === FOOTER === */
footer{background:var(--navy-dark);color:rgba(255,255,255,0.8);padding:40px 0 24px;}
.footer-inner{max-width:1100px;margin:0 auto;padding:0 40px;}
.footer-name{font-family:'Noto Serif JP',serif;font-size:1.1rem;color:var(--white);margin-bottom:8px;}
.footer-copy{font-size:0.78rem;color:rgba(255,255,255,0.5);margin-top:20px;}

/* === EDUSHIFT === */
.edushift-proposal{background:linear-gradient(135deg,#0f2440 0%,#1a3a5c 100%);padding:72px 0;}
.edushift-proposal .inner{max-width:900px;margin:0 auto;padding:0 40px;text-align:center;}
.edu-logo-tag{display:inline-block;background:rgba(200,168,60,0.18);color:var(--gold);font-size:0.75rem;font-weight:700;letter-spacing:0.14em;padding:5px 16px;border-radius:20px;border:1px solid rgba(200,168,60,0.4);margin-bottom:20px;}
.edu-title{font-family:'Noto Serif JP',serif;font-size:clamp(1.3rem,2.5vw,1.9rem);font-weight:700;color:var(--white);margin-bottom:16px;line-height:1.5;}
.edu-title span{color:var(--gold);}
.edu-desc{font-size:0.9rem;color:rgba(255,255,255,0.78);line-height:1.8;max-width:680px;margin:0 auto 36px;}
.edu-points{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:36px;}
.edu-point{background:rgba(255,255,255,0.06);border-radius:8px;padding:24px 18px;text-align:left;}
.edu-point-num{font-size:0.72rem;font-weight:700;color:var(--gold);letter-spacing:0.1em;margin-bottom:8px;}
.edu-point h4{font-size:0.9rem;font-weight:700;color:var(--white);margin-bottom:8px;}
.edu-point p{font-size:0.8rem;color:rgba(255,255,255,0.65);line-height:1.65;}
.edu-price-row{display:flex;align-items:baseline;justify-content:center;gap:14px;margin-bottom:28px;}
.edu-price{font-size:2rem;font-weight:900;color:var(--gold);font-family:'Noto Serif JP',serif;}
.edu-price small{font-size:1.1rem;}
.edu-price-note{font-size:0.78rem;color:rgba(255,255,255,0.55);}
.edu-cta{display:inline-block;background:var(--gold);color:var(--navy-dark);padding:14px 36px;border-radius:4px;font-weight:700;font-size:0.95rem;transition:background 0.2s,transform 0.2s;}
.edu-cta:hover{background:var(--gold-light);transform:translateY(-2px);}

/* === FLOATING CTA === */
.floating-cta{position:fixed;bottom:28px;right:24px;z-index:200;}
.floating-cta a{display:block;background:var(--gold);color:var(--navy-dark);padding:13px 22px;border-radius:36px;font-weight:700;font-size:0.88rem;box-shadow:0 6px 24px rgba(0,0,0,0.25);transition:background 0.2s,transform 0.2s;text-align:center;}
.floating-cta a:hover{background:var(--gold-light);transform:translateY(-3px);}

/* === RESPONSIVE === */
@media(max-width:1024px){
  .hero-content{padding:64px 32px;}
}
@media(max-width:768px){
  .nav-cta{display:none;}
  .pc-nav{display:none;}
  .hamburger{display:flex;}
  .features-grid{grid-template-columns:1fr;}
  .zz-row{grid-template-columns:1fr;}
  .zz-row.reverse .zz-img{order:0;}
  .zz-row.reverse .zz-text{order:1;}
  .zz-img{aspect-ratio:4/3;}
  .zz-text{padding:24px 20px;}
  .teacher-inner{grid-template-columns:1fr;}
  .courses-grid{grid-template-columns:1fr;}
  .flow-steps{grid-template-columns:repeat(2,1fr);}
  .flow-steps::before{display:none;}
  .access-inner{grid-template-columns:1fr;}
  .edu-points{grid-template-columns:1fr;}
  .section-inner{padding:0 20px;}
  .hero-content{padding:56px 20px;}
  .footer-inner{padding:0 20px;}
  .edushift-proposal .inner{padding:0 20px;}
}
@media(max-width:390px){
  table{font-size:0.72rem;}
  table th,table td{padding:8px 6px;}
}
"""

JS = """
(function() {
  var ham = document.getElementById('hamburger');
  var mobileNav = document.getElementById('mobile-nav');
  if (ham && mobileNav) {
    ham.addEventListener('click', function() {
      ham.classList.toggle('open');
      mobileNav.classList.toggle('open');
    });
    document.querySelectorAll('.mobile-link').forEach(function(a) {
      a.addEventListener('click', function() {
        ham.classList.remove('open');
        mobileNav.classList.remove('open');
      });
    });
  }
  (function() {
    var targets = document.querySelectorAll('.fade-in, .fade-left, .fade-right');
    var fallbackTimer = setTimeout(function() {
      targets.forEach(function(el) { el.classList.add('visible'); });
    }, 2000);
    if (!('IntersectionObserver' in window)) {
      targets.forEach(function(el) { el.classList.add('visible'); });
      clearTimeout(fallbackTimer);
      return;
    }
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    targets.forEach(function(el) { obs.observe(el); });
  })();
})();
"""

def nav_links(sections):
    links = ""
    for label, href in sections:
        links += f'<a href="#{href}">{label}</a>\n'
    return links

def mobile_nav_links(sections):
    links = ""
    for label, href in sections:
        links += f'<a href="#{href}" class="mobile-link">{label}</a>\n'
    return links

DEFAULT_NAV = [
    ("特徴", "features"),
    ("合格実績", "results"),
    ("講師紹介", "teacher"),
    ("コース・料金", "courses"),
    ("アクセス", "access"),
]

def generate_html(s, imgs):
    """Generate full HTML for a school."""
    hero_img = imgs[0]
    zz1_img = imgs[1]
    zz2_img = imgs[2]
    results_img = imgs[3]
    teacher_img = imgs[4]
    courses_img = imgs[5]

    nav_sections = s.get("nav_sections", DEFAULT_NAV)
    nav_html = nav_links(nav_sections)
    mnav_html = mobile_nav_links(nav_sections)

    # Features
    feat_html = ""
    for i, f in enumerate(s["features"]):
        icons = ["icon-star", "icon-check", "icon-bolt"]
        icon_cls = icons[i % len(icons)]
        feat_html += f'''
    <div class="feature-card fade-in">
      <div class="feature-icon"><div class="{icon_cls}"></div></div>
      <h3>{f["title"]}</h3>
      <p>{f["text"]}</p>
    </div>'''

    # Zigzag rows
    zz_imgs = [zz1_img, zz2_img, courses_img]
    zz_html = ""
    for i, row in enumerate(s["zigzag"]):
        is_odd = (i % 2 == 0)
        row_class = "zz-row" if is_odd else "zz-row reverse"
        text_fade = "fade-left" if is_odd else "fade-right"
        img_uri = zz_imgs[i] if i < len(zz_imgs) else zz_imgs[-1]
        zz_html += f'''
  <div class="{row_class}">
    <div class="zz-img">
      <img src="{img_uri}" alt="{row['h3']}" loading="lazy">
      <div class="img-overlay">写真はサンプルです。ご希望に応じて変更可能です。</div>
    </div>
    <div class="zz-text {text_fade}">
      <div class="zz-label">{row['label']}</div>
      <h3>{row['h3']}</h3>
      <p>{row['p']}</p>
    </div>
  </div>'''

    # Results groups
    results_groups_html = ""
    for grp in s["results"]["groups"]:
        items_html = "".join(f"<li>{item}</li>" for item in grp["items"])
        results_groups_html += f'''
      <div class="results-group fade-in">
        <h4>{grp['label']}</h4>
        <ul>{items_html}</ul>
      </div>'''

    # Teacher profile items
    profile_html = "".join(f"<li>{item}</li>" for item in s["teacher"]["profile"])

    # Teacher photo overlay
    overlay_text = "写真はサンプルです。ご希望に応じて変更可能です。"

    # Courses
    courses_html = ""
    for c in s["courses"]["cards"]:
        courses_html += f'''
      <div class="course-card fade-in">
        <h4>{c['name']}</h4>
        <div class="course-price">{c['price']}</div>
        <p>{c['text']}</p>
      </div>'''

    # Price table
    price_table_html = "<table>\n<thead><tr>"
    for h in s["price"]["headers"]:
        price_table_html += f"<th>{h}</th>"
    price_table_html += "</tr></thead>\n<tbody>"
    for row in s["price"]["rows"]:
        price_table_html += "<tr>"
        for cell in row:
            price_table_html += f"<td>{cell}</td>"
        price_table_html += "</tr>"
    price_table_html += "</tbody>\n</table>"

    price_notes_html = "".join(f'<span class="price-note-item">{n}</span>' for n in s["price"]["notes"])

    # Flow steps
    flow_html = ""
    for i, step in enumerate(s["flow"]):
        flow_html += f'''
      <div class="flow-step fade-in">
        <div class="step-num">{i+1:02d}</div>
        <h4>{step['title']}</h4>
        <p>{step['text']}</p>
      </div>'''

    # Map embed
    map_q = s["access"]["map_q"].replace(" ", "+")
    map_embed = f'https://maps.google.com/maps?q={map_q}&output=embed&z=16&hl=ja'

    # Access items
    access_items_html = ""
    for item in s["access"]["items"]:
        access_items_html += f'''
      <div class="access-item">
        <div class="access-icon"><div class="access-icon-inner"></div></div>
        <div>
          <div class="access-label">{item['label']}</div>
          <div class="access-val">{item['val']}</div>
        </div>
      </div>'''

    # EduShift section
    school_name_short = s["footer_name"]
    edushift_html = f'''<div class="edushift-proposal">
  <div class="inner">
    <span class="edu-logo-tag">EduShift &#183; HP制作サービス</span>
    <h2 class="edu-title">{school_name_short}のHP、<span>集客力アップ</span>しませんか？</h2>
    <p class="edu-desc">塾専門のHP制作チームが、入塾につながる導線設計でホームページをリニューアル。スマホ最適化・SEO対策・お問い合わせフォーム設置まで一括対応。月額980円〜の安心プランで、地域の保護者に選ばれる塾のWebサイトを実現します。</p>
    <div class="edu-points">
      <div class="edu-point"><div class="edu-point-num">01</div><h4>塾専門のHP制作</h4><p>学習塾の集客に特化したデザインと構成。特徴・実績・料金・アクセスを分かりやすく伝えるページを制作します。</p></div>
      <div class="edu-point"><div class="edu-point-num">02</div><h4>スマホ最適化＋集客設計</h4><p>保護者の8割以上がスマホで検索。SEO対策と問い合わせ導線を最適化し、資料請求・体験申込につなげます。</p></div>
      <div class="edu-point"><div class="edu-point-num">03</div><h4>月額980円〜の安心プラン</h4><p>保守・更新対応込み。契約縛りなしで、いつでも解約・変更可能。小規模な塾でも導入しやすい料金設計です。</p></div>
    </div>
    <div class="edu-price-row">
      <div class="edu-price">月額980円<small>〜</small></div>
      <div class="edu-price-note">保守管理費 &#183; 制作費は別途 &#183; 契約縛りなし</div>
    </div>
    <a href="https://www.edu-shift.com/service/hp-production" target="_blank" rel="noopener" class="edu-cta">EduShiftのHP制作サービスを見る</a>
  </div>
</div>'''

    css_vars = """
:root {
  --navy: #1a3a5c;
  --navy-dark: #0f2440;
  --navy-light: #2a5080;
  --gold: #c8a83c;
  --accent: #c8a83c;
  --gold-light: #e2c96a;
  --gold-dark: #a08020;
  --white: #ffffff;
  --warm-white: #f8f6f0;
  --gray-light: #ede9e0;
  --gray: #8a8a8a;
  --text: #1a3a5c;
}"""

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{s['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@600;700&display=swap" rel="stylesheet">
<style>
{css_vars}
{COMMON_CSS}
</style>
</head>
<body>

<!-- HEADER -->
<header class="site-header">
  <div class="header-inner">
    <a href="#" class="logo">{s['footer_name']}</a>
    <nav class="pc-nav">
      {nav_html}
      <a href="{s['floating_cta_href']}" class="nav-cta">{s['floating_cta_text']}</a>
    </nav>
    <button class="hamburger" id="hamburger" aria-label="メニュー">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<!-- MOBILE NAV -->
<nav id="mobile-nav">
  {mnav_html}
  <a href="{s['floating_cta_href']}" class="mobile-link" style="color:var(--gold);font-weight:700;">{s['floating_cta_text']}</a>
</nav>

<!-- HERO -->
<section class="hero" id="hero">
  <div class="hero-bg">
    <img src="{hero_img}" alt="ヒーロー画像" loading="eager">
  </div>
  <div class="hero-overlay-text">写真はサンプルです。ご希望に応じて変更可能です。</div>
  <div class="hero-content">
    <div class="hero-tag">{s['hero_tag']}</div>
    <h1>{s['hero_h1']}</h1>
    <p class="hero-sub">{s['hero_sub']}</p>
    <div class="hero-btns">
      <a href="{s['floating_cta_href']}" class="btn-primary">{s['hero_cta1']}</a>
      <a href="#courses" class="btn-outline">{s['hero_cta2']}</a>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section class="section features" id="features">
  <div class="section-inner">
    <div class="section-label">FEATURES</div>
    <h2 class="section-title">{s['footer_name']}の<span>3つの特徴</span></h2>
    <div class="features-grid">
      {feat_html}
    </div>
  </div>
</section>

<!-- ZIGZAG -->
<section class="zigzag" id="about">
  {zz_html}
</section>

<!-- RESULTS -->
<section class="section results" id="results">
  <div class="section-inner">
    <div class="section-label">ACHIEVEMENTS</div>
    <h2 class="section-title">{s['results']['year']}</h2>
    <div class="results-groups">
      {results_groups_html}
    </div>
    <div style="margin-top:32px;">
      <div class="img-wrap" style="max-width:640px;margin:0 auto;border-radius:8px;overflow:hidden;">
        <img src="{results_img}" alt="合格実績" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:cover;">
        <div class="img-overlay">写真はサンプルです。ご希望に応じて変更可能です。</div>
      </div>
    </div>
  </div>
</section>

<!-- TEACHER -->
<section class="section teacher" id="teacher">
  <div class="section-inner">
    <div class="section-label">TEACHER</div>
    <h2 class="section-title">講師紹介</h2>
    <div class="teacher-inner">
      <div class="teacher-photo-col fade-in">
        <div class="teacher-photo-wrap">
          <div class="img-wrap">
            <img src="{teacher_img}" alt="{s['teacher']['name']}" loading="lazy">
            <div class="img-overlay">{overlay_text}</div>
          </div>
        </div>
        <div class="teacher-name">{s['teacher']['name']}</div>
        <div class="teacher-title">{s['teacher']['title']}</div>
      </div>
      <div class="fade-in">
        <p class="teacher-text">{s['teacher']['text']}</p>
        <ul class="teacher-profile">
          {profile_html}
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- COURSES -->
<section class="section courses" id="courses">
  <div class="section-inner">
    <div class="section-label">COURSES</div>
    <h2 class="section-title">{s['courses']['h3']}</h2>
    <div class="courses-grid">
      {courses_html}
    </div>
    <p class="courses-note">{s['courses']['note']}</p>
  </div>
</section>

<!-- PRICE -->
<section class="section price" id="price">
  <div class="section-inner">
    <div class="section-label">PRICE</div>
    <h2 class="section-title">料金表</h2>
    {price_table_html}
    <div class="price-notes">
      {price_notes_html}
    </div>
  </div>
</section>

<!-- FLOW -->
<section class="section flow" id="flow">
  <div class="section-inner">
    <div class="section-label">FLOW</div>
    <h2 class="section-title">入塾の<span>流れ</span></h2>
    <div class="flow-steps">
      {flow_html}
    </div>
  </div>
</section>

<!-- ACCESS -->
<section class="section access" id="access">
  <div class="section-inner">
    <div class="section-label">ACCESS</div>
    <h2 class="section-title">アクセス・お問い合わせ</h2>
    <div class="access-inner">
      <div class="map-wrap fade-in">
        <iframe src="{map_embed}" allowfullscreen="" loading="lazy" title="地図"></iframe>
      </div>
      <div class="access-info fade-in">
        <h4>{s['footer_name']}</h4>
        {access_items_html}
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-name">{s['footer_name']}</div>
    <p class="footer-copy">&copy; 2025 {s['footer_name']} All Rights Reserved.</p>
  </div>
</footer>

{edushift_html}

<!-- FLOATING CTA -->
<div class="floating-cta">
  <a href="{s['floating_cta_href']}">{s['floating_cta_text']}</a>
</div>

<script>
{JS}
</script>
</body>
</html>"""
    return html


# ============================================================
# School data definitions
# ============================================================

SCHOOLS = [
    # ----------------------------------------------------------
    # 1. shounan-a.html
    # ----------------------------------------------------------
    {
        "filename": "shounan-a.html",
        "img_indices": [6, 14, 11, 8, 0, 18],
        "title": "湘南スクール | 横浜・葉山・横須賀の個別指導塾",
        "footer_name": "湘南スクール",
        "hero_tag": "25年連続 志望校全員合格",
        "hero_h1": "生徒に<span>寄り添う</span>個別指導で、<br>夢の志望校へ",
        "hero_sub": "「みまもる先生」が生徒2〜3人に1人つき、答えを見付けるまで徹底サポート。横浜・葉山・横須賀・オンラインで、あなたの学習をしっかり支えます。",
        "hero_cta1": "無料体験を申し込む",
        "hero_cta2": "料金を見る",
        "features": [
            {"title": "みまもる先生制", "text": "生徒2〜3人に先生1人が徹底サポート。答えを見付けるまで寄り添う指導スタイルで、理解を深めます。"},
            {"title": "25年連続 全員合格", "text": "開塾以来、志望校全員合格を達成。豊富な受験指導実績で安心してお子様を任せられます。"},
            {"title": "オンライン授業対応", "text": "対面(横浜・葉山・横須賀)とオンラインを選べる柔軟な受講形式。遠方の方にも対応します。"},
        ],
        "zigzag": [
            {"label": "OUR STYLE", "h3": "答えを見つけるまで、先生がそばにいる", "p": "「みまもる先生制」により、生徒2〜3人に先生が1人つき常に寄り添います。理解が深まるまで丁寧に指導し、「わかった！」の瞬間を一緒に積み重ねます。"},
            {"label": "OUR STRENGTH", "h3": "25年連続 志望校全員合格の実績", "p": "湘南スクールは創業以来、受験生の志望校全員合格を達成し続けています。東大・早慶はもちろん、湘南高校・横須賀高校・柏陽高校など地域トップ校への合格実績多数。"},
            {"label": "ONLINE CLASS", "h3": "対面とオンライン、選べる授業形式", "p": "横浜・葉山・横須賀の各教室に加え、自宅から受講できるオンライン教室も完備。生活スタイルや状況に合わせて、最適な受講形式をお選びいただけます。"},
        ],
        "results": {
            "year": "2025年度 合格実績",
            "groups": [
                {"label": "国公立・難関大", "items": ["東京大学", "東工大", "大阪大学", "早稲田大学", "慶應義塾大学"]},
                {"label": "公立高校", "items": ["湘南高校", "横須賀高校", "柏陽高校", "鎌倉高校", "横浜翠嵐高校"]},
            ],
        },
        "teacher": {
            "name": "鈴木道彦",
            "title": "塾長",
            "text": "「みまもる先生」の考えのもと、一人ひとりの生徒が自信を持って学べる環境を大切にしています。25年以上の指導実績で積み重ねた独自のメソッドで、志望校合格をサポートします。",
            "profile": ["指導歴25年以上", "横浜・葉山・横須賀・オンライン4教室運営", "志望校全員合格25年連続達成"],
        },
        "courses": {
            "h3": "コース・時間割",
            "cards": [
                {"name": "小学生コース", "price": "月額10,000円〜", "text": "教科・曜日・時間は相談の上決定。基礎固めから中学受験まで対応。"},
                {"name": "中学生コース", "price": "月額13,000円〜", "text": "定期テスト対策・高校受験まで一貫指導。"},
                {"name": "高校生コース", "price": "月額15,000円〜", "text": "大学受験対策・推薦入試まで幅広く対応。"},
            ],
            "note": "授業時間・曜日は生徒の都合に合わせて柔軟に設定。詳細はお問い合わせください。",
        },
        "price": {
            "headers": ["学年", "週1回", "週2回", "週3回"],
            "rows": [
                ["小学生", "10,000円", "18,000円", "25,000円"],
                ["中学生", "13,000円", "23,000円", "32,000円"],
                ["高校生", "15,000円", "27,000円", "37,000円"],
            ],
            "notes": ["入塾金：別途", "テキスト代：実費", "季節講習：別途"],
        },
        "flow": [
            {"title": "お問い合わせ", "text": "電話・メール・フォームでご連絡ください"},
            {"title": "無料体験授業", "text": "実際の授業を体験いただけます"},
            {"title": "面談・ご入塾", "text": "学習状況を確認し、プランを決定"},
            {"title": "学習スタート", "text": "志望校合格に向けて始動！"},
        ],
        "access": {
            "map_q": "横浜市栄区飯島町1398",
            "items": [
                {"label": "住所", "val": "神奈川県横浜市栄区飯島町1398-8（横浜校）<br>三浦郡葉山町堀内899-5（葉山・元町校）"},
                {"label": "電話", "val": "045-893-7900"},
                {"label": "メール", "val": "shounan@jcom.home.ne.jp"},
                {"label": "営業時間", "val": "平日15:00〜22:00 / 土曜10:00〜18:00"},
            ],
        },
        "floating_cta_text": "無料体験を申し込む",
        "floating_cta_href": "mailto:shounan@jcom.home.ne.jp",
    },

    # ----------------------------------------------------------
    # 2. nakamaruko-a.html
    # ----------------------------------------------------------
    {
        "filename": "nakamaruko-a.html",
        "img_indices": [9, 15, 12, 6, 1, 19],
        "title": "地元の個別指導塾 中丸子校 | 川崎市中原区の個別指導塾",
        "footer_name": "地元の個別指導塾 中丸子校",
        "hero_tag": "完全1:2 個別指導",
        "hero_h1": "お子さんの<span>「もう一つの居場所」</span>に",
        "hero_sub": "川崎市中原区・平間エリアの個別指導塾。完全1対2の丁寧な指導で、小さな成功体験を積み重ね、自信と学力を育てます。",
        "hero_cta1": "無料体験を申し込む",
        "hero_cta2": "料金を見る",
        "features": [
            {"title": "完全1対2 個別指導", "text": "先生1人に生徒2人まで。一人ひとりに目が届く環境で、理解度に合わせた指導を行います。"},
            {"title": "もう一つの居場所", "text": "勉強だけでなく、生徒の気持ちにも寄り添う温かな塾。失敗も成功のもと、安心して通えます。"},
            {"title": "LINE相談対応", "text": "保護者の方からのご質問・ご相談をLINEで受け付け。すぐに対応できる体制で安心をお届けします。"},
        ],
        "zigzag": [
            {"label": "OUR APPROACH", "h3": "小さな成功体験が、大きな自信になる", "p": "「できた！」という喜びを積み重ねることが、学習意欲につながります。つまずきを一緒に解決し、一歩一歩確実に前進できる指導を心がけています。"},
            {"label": "ENVIRONMENT", "h3": "失敗を恐れず挑戦できる環境", "p": "失敗は成功のもと。間違えることを恐れず、積極的に問題に向き合える雰囲気づくりを大切にしています。校長・一森がしっかり見守ります。"},
            {"label": "SUPPORT", "h3": "保護者との連携で家庭学習もサポート", "p": "LINEでのご相談を随時受け付け。授業の進捗や家庭学習のアドバイスを通じて、塾と家庭が一体となった学習支援を行います。"},
        ],
        "results": {
            "year": "主な進学先",
            "groups": [
                {"label": "中学受験", "items": ["地域公立中学", "私立中学受験対応"]},
                {"label": "高校受験", "items": ["川崎市内公立高校", "私立高校"]},
            ],
        },
        "teacher": {
            "name": "一森（いちもり）",
            "title": "校長",
            "text": "教育業界10年以上の経験をもとに、「もう一つの居場所」となる塾づくりを目指しています。生徒一人ひとりの性格や学習スタイルを大切にした指導で、確実な成長をサポートします。",
            "profile": ["教育業界10年以上", "完全1対2個別指導", "川崎市中原区密着", "LINE相談対応"],
        },
        "courses": {
            "h3": "コース・料金",
            "cards": [
                {"name": "小学生コース", "price": "お問い合わせください", "text": "基礎から応用まで対応。学校の授業の先取り・復習に。"},
                {"name": "中学生コース", "price": "お問い合わせください", "text": "定期テスト対策から高校受験まで一貫指導。"},
                {"name": "高校生コース", "price": "お問い合わせください", "text": "大学受験・推薦入試もしっかりサポート。"},
            ],
            "note": "料金・時間割は個別相談の上決定。まずはお気軽にお問い合わせください。",
        },
        "price": {
            "headers": ["コース", "指導形態", "月額料金"],
            "rows": [
                ["小学生", "1対2個別", "要相談"],
                ["中学生", "1対2個別", "要相談"],
                ["高校生", "1対2個別", "要相談"],
            ],
            "notes": ["詳細はお問い合わせください", "無料体験授業実施中"],
        },
        "flow": [
            {"title": "お問い合わせ", "text": "電話・メール・フォームでご連絡ください"},
            {"title": "無料体験授業", "text": "実際の授業を体験いただけます"},
            {"title": "面談・ご入塾", "text": "学習状況を確認し、プランを決定"},
            {"title": "学習スタート", "text": "自信と学力を育てる学習をスタート！"},
        ],
        "access": {
            "map_q": "川崎市中原区中丸子",
            "items": [
                {"label": "住所", "val": "川崎市中原区（平間エリア）"},
                {"label": "電話", "val": "電話はお問い合わせフォームよりご確認ください"},
                {"label": "営業時間", "val": "平日15:00〜22:00"},
            ],
        },
        "floating_cta_text": "LINE相談・無料体験申込",
        "floating_cta_href": "#access",
    },

    # ----------------------------------------------------------
    # 3. chikyujuku-a.html
    # ----------------------------------------------------------
    {
        "filename": "chikyujuku-a.html",
        "img_indices": [7, 16, 13, 9, 2, 17],
        "title": "知求塾 | さいたま市の自立型個別指導塾",
        "footer_name": "知求塾",
        "hero_tag": "限定7名 自立型個別指導",
        "hero_h1": "自ら考え、<span>能動的に学ぶ力</span>を育てる",
        "hero_sub": "さいたま市見沼区（東大宮・七里）の少人数個別指導塾。定員7名の環境で、自ら考え主体的に学習する習慣を徹底的に育てます。",
        "hero_cta1": "4回無料体験を申し込む",
        "hero_cta2": "コースを見る",
        "features": [
            {"title": "限定7名の少人数制", "text": "定員7名の完全少人数制。一人ひとりに目が届き、きめ細かな指導が可能です。"},
            {"title": "自立型学習指導", "text": "答えを教えるのではなく、自ら考える力を育てる指導。問題解決能力・思考力が身につきます。"},
            {"title": "4回無料体験", "text": "入塾前に4回の無料体験を実施。じっくり体験してからご判断いただけます。"},
        ],
        "zigzag": [
            {"label": "OUR PHILOSOPHY", "h3": "答えを教えない、考える力を育てる", "p": "「教えすぎない指導」が知求塾の根本方針。ヒントを出しながら自分で考え、自分で解答に辿り着く達成感を積み重ねることで、本物の学力を育てます。"},
            {"label": "RESULTS 2026", "h3": "2026年度 合格実績：地域トップ校に多数合格", "p": "不動岡1名、浦和西1名、浦和東3名、大宮東2名、大宮南3名、大宮商業6名など、さいたま・埼玉県内の主要高校に多数合格。私立も武南・埼玉栄・淑徳与野など。"},
            {"label": "SPRING PROGRAM", "h3": "春期講習・無料体験で塾の雰囲気をお試しください", "p": "3月27日〜4月7日の春期講習を実施中。入塾を検討している方は4回無料体験を活用ください。先着7名限定で入塾金免除キャンペーンも実施中。"},
        ],
        "results": {
            "year": "2026年度 合格実績",
            "groups": [
                {"label": "公立高校", "items": ["不動岡高校1名", "浦和西高校1名", "浦和東高校3名", "大宮東高校2名", "大宮南高校3名", "大宮商業高校6名"]},
                {"label": "私立高校", "items": ["武南高校", "埼玉栄高校", "淑徳与野高校", "浦和学院高校"]},
            ],
        },
        "teacher": {
            "name": "塾長",
            "title": "知求塾代表",
            "text": "自ら考え、能動的に学ぶ習慣こそが、受験だけでなく社会に出ても通用する真の学力だと信じています。少人数制だからこそできる、一人ひとりに寄り添った丁寧な指導を提供します。",
            "profile": ["さいたま市見沼区地域密着", "限定7名少人数制指導", "4回無料体験制度"],
        },
        "courses": {
            "h3": "コース・料金",
            "cards": [
                {"name": "中学生コース", "price": "お問い合わせください", "text": "自立型個別指導。高校受験対策から定期テスト対策まで。"},
                {"name": "高校生コース", "price": "お問い合わせください", "text": "大学受験対策。国公立・難関私大を目指す方へ。"},
                {"name": "小学生コース", "price": "お問い合わせください", "text": "中学受験・基礎学力向上。"},
            ],
            "note": "春期講習3/27〜4/7実施中。先着7名入塾金免除。",
        },
        "price": {
            "headers": ["コース", "週1回", "週2回"],
            "rows": [
                ["中学生", "要相談", "要相談"],
                ["高校生", "要相談", "要相談"],
            ],
            "notes": ["入塾金免除（先着7名）", "4回無料体験あり"],
        },
        "flow": [
            {"title": "お問い合わせ", "text": "電話・メール・フォームでご連絡ください"},
            {"title": "4回無料体験", "text": "じっくり4回体験してから判断できます"},
            {"title": "面談・ご入塾", "text": "学習状況を確認し、プランを決定"},
            {"title": "学習スタート", "text": "自立型学習で本物の学力を育てます"},
        ],
        "access": {
            "map_q": "さいたま市見沼区東大宮",
            "items": [
                {"label": "住所", "val": "さいたま市見沼区東大宮・七里エリア"},
                {"label": "電話", "val": "お問い合わせフォームよりご連絡ください"},
                {"label": "営業時間", "val": "平日16:00〜22:00"},
            ],
        },
        "floating_cta_text": "4回無料体験を申し込む",
        "floating_cta_href": "#access",
    },

    # ----------------------------------------------------------
    # 4. shogakukai-a.html
    # ----------------------------------------------------------
    {
        "filename": "shogakukai-a.html",
        "img_indices": [10, 14, 11, 7, 3, 18],
        "title": "荘学会ゼミナール | 鶴岡市の完全1対1個別指導塾",
        "footer_name": "荘学会ゼミナール",
        "hero_tag": "完全1:1 個別指導",
        "hero_h1": "マンツーマンで<span>確実に</span>成績を上げる",
        "hero_sub": "山形県鶴岡市の完全1対1個別指導塾。テキスト代・教材費不要、入会費・入塾金不要で、安心してお子様の学習をお任せください。",
        "hero_cta1": "無料体験を申し込む",
        "hero_cta2": "料金を見る",
        "features": [
            {"title": "完全1対1指導", "text": "先生と生徒がマンツーマンで向き合う完全個別指導。生徒のペースに合わせた最適な授業を提供します。"},
            {"title": "費用がわかりやすい", "text": "テキスト代・教材費・入会費・入塾金すべて不要。月額料金だけのシンプルな料金体系です。"},
            {"title": "最新教育理論を活用", "text": "学習科学に基づいた指導法と充実した学習環境で、効率的に成績アップを実現します。"},
        ],
        "zigzag": [
            {"label": "1 ON 1 TEACHING", "h3": "完全マンツーマンだから、疑問をすぐ解決", "p": "1対1の指導だからこそ、授業中に湧いた疑問をその場で解決できます。理解度に合わせてスピードを調整し、置いてきぼりにならない学習を実現します。"},
            {"label": "NO HIDDEN FEES", "h3": "入塾金・テキスト代すべて無料", "p": "荘学会ゼミナールでは、入会費・入塾金・テキスト代・教材費はいただきません。月額料金のみのわかりやすい料金体系で、安心してご利用いただけます。"},
            {"label": "ENVIRONMENT", "h3": "鶴岡市役所より徒歩5分の好立地", "p": "鶴岡市役所から徒歩5分という通いやすい立地。放課後や学校帰りに気軽に立ち寄れる環境を整えています。"},
        ],
        "results": {
            "year": "主な合格実績",
            "groups": [
                {"label": "公立高校", "items": ["鶴岡南高校", "鶴岡北高校", "酒田東高校"]},
                {"label": "大学", "items": ["山形大学", "東北地方国公立大学"]},
            ],
        },
        "teacher": {
            "name": "塾長",
            "title": "荘学会ゼミナール代表",
            "text": "生徒一人ひとりの個性と学習スタイルを大切にした指導を心がけています。完全1対1だからこそできる、きめ細かなサポートで確実な成績向上を目指します。",
            "profile": ["鶴岡市地域密着", "完全1対1個別指導", "入塾金・テキスト代不要"],
        },
        "courses": {
            "h3": "コース・料金",
            "cards": [
                {"name": "小学生コース", "price": "月額8,000円〜(90分)", "text": "基礎学力の向上。算数・国語を中心に指導。"},
                {"name": "中学生コース", "price": "月額10,000円〜(120分)", "text": "定期テスト対策・高校受験対策。"},
                {"name": "高校生コース", "price": "月額10,000円〜(120分)", "text": "大学受験・推薦入試対策。"},
            ],
            "note": "テキスト代・教材費・入会費・入塾金すべて無料。",
        },
        "price": {
            "headers": ["学年", "授業時間", "月額料金"],
            "rows": [
                ["小学生", "90分/回", "8,000円〜"],
                ["中学生", "120分/回", "10,000円〜"],
                ["高校生", "120分/回", "10,000円〜"],
            ],
            "notes": ["テキスト代不要", "入会費不要", "入塾金不要"],
        },
        "flow": [
            {"title": "お問い合わせ", "text": "電話・LINEにてご連絡ください"},
            {"title": "無料体験授業", "text": "実際の授業を体験いただけます"},
            {"title": "面談・ご入塾", "text": "学習状況を確認し、プランを決定"},
            {"title": "学習スタート", "text": "マンツーマンで確実に成績アップ！"},
        ],
        "access": {
            "map_q": "鶴岡市役所 山形県鶴岡市",
            "items": [
                {"label": "住所", "val": "山形県鶴岡市（鶴岡市役所より徒歩5分）"},
                {"label": "電話", "val": "電話・LINEにてお問い合わせください"},
                {"label": "営業時間", "val": "平日15:00〜22:00 / 土曜10:00〜18:00"},
            ],
        },
        "floating_cta_text": "無料体験を申し込む",
        "floating_cta_href": "#access",
    },

    # ----------------------------------------------------------
    # 5. manabiya-a.html
    # ----------------------------------------------------------
    {
        "filename": "manabiya-a.html",
        "img_indices": [8, 15, 12, 10, 4, 16],
        "title": "学びや | 新神戸駅徒歩5分の個別指導塾",
        "footer_name": "学びや",
        "hero_tag": "灘高→京大卒の塾長が直接指導",
        "hero_h1": "<span>本物の学力</span>を、神戸から",
        "hero_sub": "神戸市中央区・新神戸駅徒歩5分。灘高校→京都大学理学部卒・元キムラタン社長の塾長が直接指導。英会話レッスン（外国人講師）も好評開催中。",
        "hero_cta1": "無料体験を申し込む",
        "hero_cta2": "料金を見る",
        "features": [
            {"title": "灘高→京大卒 塾長直接指導", "text": "塾長・浅川岳彦が直接指導。灘高校から京都大学理学部への実体験に基づいた、実践的な学習メソッドを提供します。"},
            {"title": "英会話レッスン", "text": "外国人講師マーセルによる英会話レッスンを開講。月4回7,000円〜で本格的な英語力を養います。"},
            {"title": "新神戸駅徒歩5分", "text": "三宮・新神戸からアクセス抜群。放課後に気軽に通える好立地です。"},
        ],
        "zigzag": [
            {"label": "PRINCIPAL", "h3": "灘高→京大卒の塾長が、直接教えます", "p": "塾長・浅川岳彦は、灘高校から京都大学理学部に進学。大学卒業後は実業界で活躍し、キムラタン社長も経験。豊富な人生経験と確かな学力で、子どもたちの未来を支えます。"},
            {"label": "ENGLISH", "h3": "外国人講師による本格英会話レッスン", "p": "外国人講師マーセルによる英会話レッスンを毎月開催。月4回7,000円・月8回13,000円の2プランで、生きた英語力を磨きます。小学生から高校生まで対応。"},
            {"label": "LOCATION", "h3": "新神戸駅から徒歩5分の好立地", "p": "神戸市中央区熊内町4-5-2 第3熊内コーポラス1階。新神戸駅から徒歩5分で通いやすく、JR・地下鉄からのアクセスも良好です。"},
        ],
        "results": {
            "year": "主な進学実績",
            "groups": [
                {"label": "大学", "items": ["関西圏国公立大学", "関関同立", "MARCH"]},
                {"label": "高校", "items": ["兵庫県内公私立高校"]},
            ],
        },
        "teacher": {
            "name": "浅川岳彦",
            "title": "塾長",
            "text": "灘高校→京都大学理学部という自身の学習経験を活かした実践的な指導が特長。「わかる楽しさ」を伝えながら、一人ひとりの可能性を引き出します。英会話クラスも運営し、総合的な学力向上を支援します。",
            "profile": ["灘高校→京都大学理学部卒", "元キムラタン社長", "英会話クラス（外国人講師）運営", "小中高全学年対応"],
        },
        "courses": {
            "h3": "コース・料金",
            "cards": [
                {"name": "個別指導コース", "price": "月額8,000円〜", "text": "小中高対応。科目・曜日・時間は相談の上決定。"},
                {"name": "英会話コース（月4回）", "price": "月額7,000円", "text": "外国人講師マーセルによる英会話レッスン。"},
                {"name": "英会話コース（月8回）", "price": "月額13,000円", "text": "集中的に英会話力を高めたい方へ。"},
            ],
            "note": "複数コース同時受講可。詳細はお問い合わせください。",
        },
        "price": {
            "headers": ["コース", "内容", "月額料金"],
            "rows": [
                ["個別指導", "小中高・全科目", "8,000円〜"],
                ["英会話(月4回)", "外国人講師", "7,000円"],
                ["英会話(月8回)", "外国人講師", "13,000円"],
            ],
            "notes": ["体験授業あり", "詳細はお問い合わせください"],
        },
        "flow": [
            {"title": "お問い合わせ", "text": "電話・メールでご連絡ください"},
            {"title": "無料体験授業", "text": "実際の授業を体験いただけます"},
            {"title": "面談・ご入塾", "text": "学習状況を確認し、プランを決定"},
            {"title": "学習スタート", "text": "本物の学力を神戸から育てます！"},
        ],
        "access": {
            "map_q": "神戸市中央区熊内町4",
            "items": [
                {"label": "住所", "val": "神戸市中央区熊内町4-5-2 第3熊内コーポラス1階（新神戸駅徒歩5分）"},
                {"label": "電話", "val": "070-1741-5123"},
                {"label": "メール", "val": "manabiya5123@gmail.com"},
                {"label": "営業時間", "val": "平日15:00〜22:00 / 土曜10:00〜18:00"},
            ],
        },
        "floating_cta_text": "無料体験を申し込む",
        "floating_cta_href": "mailto:manabiya5123@gmail.com",
    },
]


def main():
    print("Loading images...")
    all_img_uris = [read_img(name) for name in IMAGE_NAMES]
    print(f"  Loaded {len(all_img_uris)} images.")

    for school in SCHOOLS:
        print(f"Generating {school['filename']}...")
        imgs = [all_img_uris[i] for i in school["img_indices"]]
        html = generate_html(school, imgs)
        out_path = os.path.join(OUT_DIR, school["filename"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        size_kb = os.path.getsize(out_path) / 1024
        print(f"  -> {out_path}  ({size_kb:.1f} KB)")

    print("\n=== Verification ===")
    all_ok = True
    for school in SCHOOLS:
        path = os.path.join(OUT_DIR, school["filename"])
        if os.path.exists(path):
            size = os.path.getsize(path)
            size_kb = size / 1024
            status = "OK" if size >= 200 * 1024 else "SMALL"
            print(f"  [{status}] {school['filename']}  {size_kb:.1f} KB")
            if size < 200 * 1024:
                all_ok = False
        else:
            print(f"  [MISSING] {school['filename']}")
            all_ok = False

    if all_ok:
        print("\nDONE")
    else:
        print("\nWARNING: Some files may be too small or missing.")


if __name__ == "__main__":
    main()
