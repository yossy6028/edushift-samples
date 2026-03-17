#!/usr/bin/env python3
"""
gen_schools_b.py
Generate 5 HTML sample pages (A variants) for Japanese cram schools.
Batch: maedajuku-a, cad-a, nix-a, azumajuku-a, suzuki-a
"""

import os
import base64

# ── paths ──────────────────────────────────────────────────────────────
B64_DIR = "/Users/yossy/.openclaw/workspace-nanami/projects/pj1/images/library/b64"
OUT_DIR = "/Users/yossy/edushift-samples"

# ── image library (index → filename without extension) ─────────────────
IMAGE_LIB = [
    "classroom_exam-schedule-01",        # 0
    "classroom_reception-achievement-01",# 1
    "classroom_study-corner-01",         # 2
    "classroom_waiting-area-01",         # 3
    "exam_stationery-01",               # 4
    "hero_individual-tutor-01",         # 5
    "hero_modern-study-01",             # 6
    "hero_partitioned-desk-01",         # 7
    "hero_self-study-01",              # 8
    "hero_test-prep-01",               # 9
    "hero_warm-entrance-01",           # 10
    "study_compact-partitioned-01",    # 11
    "study_desk-closeup-01",           # 12
    "study_math-help-01",              # 13
    "study_row-desks-01",              # 14
    "study_rural-tutor-01",            # 15
    "study_small-group-01",            # 16
    "study_stationery-01",             # 17
    "study_tutor-elementary-01",       # 18
    "support_tools-01",                # 19
]

def load_b64(index):
    """Return data URI string for image at given library index."""
    name = IMAGE_LIB[index]
    path = os.path.join(B64_DIR, name + ".b64")
    with open(path, "r") as f:
        raw = f.read().strip()
    # File may already include the data URI prefix or just raw base64
    if raw.startswith("data:"):
        return raw
    return f"data:image/jpeg;base64,{raw}"


IMG_OVERLAY_TEXT = "写真はサンプルです。ご希望に応じて変更可能です。"
EDUSHIFT_URL = "https://www.edu-shift.com/service/hp-production"


# ════════════════════════════════════════════════════════════════════════
# HTML GENERATION
# ════════════════════════════════════════════════════════════════════════

def edushift_section(school_name):
    return f"""<div class="edushift-proposal">
  <div class="inner">
    <span class="edu-logo-tag">EduShift &#183; HP制作サービス</span>
    <h2 class="edu-title">{school_name}のHP、<span>集客力アップ</span>しませんか？</h2>
    <p class="edu-desc">塾専門のHP制作チームが、入塾につながる導線設計でホームページをリニューアル。月額980円〜の安心プランで、地域の保護者に選ばれる塾のWebサイトを実現します。</p>
    <div class="edu-points">
      <div class="edu-point"><div class="edu-point-num">01</div><h4>塾専門のHP制作</h4><p>学習塾の集客に特化したデザイン。</p></div>
      <div class="edu-point"><div class="edu-point-num">02</div><h4>スマホ最適化</h4><p>保護者の8割がスマホで検索。最適化対応。</p></div>
      <div class="edu-point"><div class="edu-point-num">03</div><h4>月額980円〜</h4><p>契約縛りなし。安心プラン。</p></div>
    </div>
    <div class="edu-price-row"><div class="edu-price">月額980円<small>〜</small></div></div>
    <a href="{EDUSHIFT_URL}" target="_blank" rel="noopener" class="edu-cta">EduShiftのHP制作サービスを見る</a>
  </div>
</div>"""


JS_BLOCK = """<script>
(function() {
  var ham = document.getElementById('hamburger');
  var mobileNav = document.getElementById('mobile-nav');
  if (ham && mobileNav) {
    ham.addEventListener('click', function() { ham.classList.toggle('open'); mobileNav.classList.toggle('open'); });
    document.querySelectorAll('.mobile-link').forEach(function(a) {
      a.addEventListener('click', function() { ham.classList.remove('open'); mobileNav.classList.remove('open'); });
    });
  }
  (function() {
    var targets = document.querySelectorAll('.fade-in, .fade-left, .fade-right');
    var fallbackTimer = setTimeout(function() { targets.forEach(function(el) { el.classList.add('visible'); }); }, 2000);
    if (!('IntersectionObserver' in window)) { targets.forEach(function(el) { el.classList.add('visible'); }); clearTimeout(fallbackTimer); return; }
    var obs = new IntersectionObserver(function(entries) { entries.forEach(function(entry) { if (entry.isIntersecting) { entry.target.classList.add('visible'); obs.unobserve(entry.target); } }); }, { threshold: 0.1 });
    targets.forEach(function(el) { obs.observe(el); });
  })();
})();
</script>"""


CSS = """:root {
  --navy: #1a3a5c;
  --navy-dark: #0f2440;
  --navy-light: #2a5080;
  --gold: #c8a83c; --accent: #c8a83c;
  --gold-light: #e2c96a;
  --gold-dark: #a08020;
  --white: #ffffff;
  --warm-white: #f8f6f0;
  --gray-light: #ede9e0;
  --gray: #8a8a8a;
  --text: #1a3a5c;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;overflow-x:hidden;}
body{font-family:'Noto Sans JP',sans-serif;color:var(--text);background:var(--white);line-height:1.7;}

/* ANIMATIONS */
.fade-in{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade-left{opacity:0;transform:translateX(-40px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade-right{opacity:0;transform:translateX(40px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade-in.visible,.fade-left.visible,.fade-right.visible{opacity:1;transform:none;}

/* IMG WRAP */
.img-wrap{position:relative;overflow:hidden;}
.img-overlay{position:absolute;bottom:0;left:0;background:rgba(0,0,0,0.55);color:#fff;font-size:0.7rem;padding:2px 8px;width:100%;box-sizing:border-box;text-align:center;pointer-events:none;}

/* HEADER */
header{position:fixed;top:0;left:0;width:100%;background:var(--navy-dark);z-index:1000;box-shadow:0 2px 8px rgba(0,0,0,0.3);}
.header-inner{max-width:1200px;margin:0 auto;padding:0 24px;height:68px;display:flex;align-items:center;justify-content:space-between;}
.logo{color:var(--white);font-family:'Noto Serif JP',serif;font-size:1.2rem;font-weight:700;text-decoration:none;letter-spacing:0.05em;}
.logo span{color:var(--gold);}
nav.pc-nav{display:flex;align-items:center;gap:20px;}
nav.pc-nav a{color:var(--white);text-decoration:none;font-size:0.88rem;transition:color 0.2s;}
nav.pc-nav a:hover{color:var(--gold);}
.nav-cta{background:var(--gold);color:var(--navy-dark) !important;padding:8px 20px;border-radius:4px;font-weight:700;font-size:0.88rem;transition:background 0.2s !important;}
.nav-cta:hover{background:var(--gold-light) !important;}

/* HAMBURGER */
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:8px;}
.hamburger span{display:block;width:26px;height:2px;background:var(--white);transition:all 0.3s;border-radius:2px;}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
.hamburger.open span:nth-child(2){opacity:0;}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}

/* MOBILE NAV */
#mobile-nav{display:none;position:fixed;top:68px;left:0;width:100%;background:var(--navy-dark);z-index:999;padding:20px 24px;flex-direction:column;gap:0;}
#mobile-nav.open{display:flex;}
.mobile-link{color:var(--white);text-decoration:none;font-size:1rem;padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.1);display:block;}
.mobile-link:last-child{border-bottom:none;}
.mobile-cta-link{background:var(--gold);color:var(--navy-dark) !important;text-align:center;padding:14px;border-radius:4px;margin-top:12px;font-weight:700;}

/* HERO */
.hero{position:relative;height:100vh;min-height:600px;overflow:hidden;}
.hero-img{position:absolute;inset:0;}
.hero-img img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(135deg,rgba(10,26,64,0.80) 0%,rgba(10,26,64,0.55) 100%);}
.hero-content{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;padding:0 60px;max-width:900px;}
.hero-tag{background:var(--gold);color:var(--navy-dark);font-size:0.85rem;font-weight:700;padding:4px 14px;border-radius:2px;margin-bottom:20px;display:inline-block;letter-spacing:0.08em;}
.hero h1{font-family:'Noto Serif JP',serif;font-size:clamp(2rem,5vw,3.4rem);font-weight:700;color:var(--white);line-height:1.35;margin-bottom:20px;}
.hero h1 span{color:var(--gold);}
.hero-sub{color:rgba(255,255,255,0.88);font-size:clamp(0.92rem,1.8vw,1.1rem);margin-bottom:36px;line-height:1.8;max-width:600px;}
.hero-btns{display:flex;gap:16px;flex-wrap:wrap;}
.btn-primary{background:var(--gold);color:var(--navy-dark);padding:15px 36px;border-radius:4px;text-decoration:none;font-weight:700;font-size:1rem;transition:background 0.2s,transform 0.2s;display:inline-block;white-space:nowrap;}
.btn-primary:hover{background:var(--gold-light);transform:translateY(-2px);}
.btn-secondary{background:transparent;color:var(--white);padding:14px 36px;border-radius:4px;border:2px solid var(--white);text-decoration:none;font-weight:700;font-size:1rem;transition:background 0.2s,transform 0.2s;display:inline-block;white-space:nowrap;}
.btn-secondary:hover{background:rgba(255,255,255,0.15);transform:translateY(-2px);}

/* SECTIONS COMMON */
section{padding:80px 24px;}
.section-inner{max-width:1100px;margin:0 auto;}
.section-label{font-size:0.8rem;font-weight:700;letter-spacing:0.15em;color:var(--gold-dark);text-transform:uppercase;margin-bottom:10px;}
.section-title{font-family:'Noto Serif JP',serif;font-size:clamp(1.6rem,3.5vw,2.4rem);font-weight:700;color:var(--navy);margin-bottom:16px;}
.section-title span{color:var(--gold-dark);}
.section-desc{color:var(--gray);font-size:1rem;max-width:640px;line-height:1.8;margin-bottom:48px;}

/* FEATURES */
.features{background:var(--warm-white);}
.features-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;}
.feature-card{background:var(--white);border-radius:8px;padding:36px 28px;box-shadow:0 2px 12px rgba(26,58,92,0.08);border-top:4px solid var(--gold);}
.feature-icon{width:52px;height:52px;background:var(--navy);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px;position:relative;}
.feature-icon::after{content:'';position:absolute;width:20px;height:20px;background:var(--gold);border-radius:3px;transform:rotate(45deg);}
.feature-num{font-size:0.78rem;font-weight:700;letter-spacing:0.12em;color:var(--gold-dark);margin-bottom:8px;}
.feature-card h3{font-family:'Noto Serif JP',serif;font-size:1.1rem;font-weight:700;color:var(--navy);margin-bottom:12px;}
.feature-card p{color:var(--gray);font-size:0.91rem;line-height:1.75;}

/* ZIGZAG */
.zigzag{background:var(--white);}
.zz-row{display:grid;grid-template-columns:1fr 1fr;gap:0;align-items:stretch;margin-bottom:0;}
.zz-row:nth-child(odd) .zz-img{order:1;}
.zz-row:nth-child(odd) .zz-text{order:2;}
.zz-row:nth-child(even) .zz-img{order:2;}
.zz-row:nth-child(even) .zz-text{order:1;}
.zz-img .img-wrap{height:100%;min-height:320px;aspect-ratio:4/3;}
.zz-img .img-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.zz-text{padding:56px;display:flex;flex-direction:column;justify-content:center;background:var(--warm-white);}
.zz-row:nth-child(even) .zz-text{background:var(--navy-dark);}
.zz-row:nth-child(even) .zz-text .zz-label{color:var(--gold-light);}
.zz-row:nth-child(even) .zz-text h3{color:var(--white);}
.zz-row:nth-child(even) .zz-text p{color:rgba(255,255,255,0.82);}
.zz-label{font-size:0.78rem;font-weight:700;letter-spacing:0.15em;color:var(--gold-dark);text-transform:uppercase;margin-bottom:12px;}
.zz-text h3{font-family:'Noto Serif JP',serif;font-size:clamp(1.2rem,2.5vw,1.65rem);font-weight:700;color:var(--navy);margin-bottom:16px;line-height:1.4;}
.zz-text p{font-size:0.93rem;color:var(--gray);line-height:1.85;}

/* RESULTS */
.results{background:var(--navy-dark);padding:80px 24px;}
.results .section-title{color:var(--white);}
.results .section-label{color:var(--gold-light);}
.results .section-desc{color:rgba(255,255,255,0.75);}
.results-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
.results-img{aspect-ratio:4/3;border-radius:8px;overflow:hidden;}
.results-img .img-wrap{width:100%;height:100%;}
.results-img .img-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.results-content{color:var(--white);}
.results-year{font-size:1rem;font-weight:700;color:var(--gold);margin-bottom:20px;letter-spacing:0.05em;border-left:4px solid var(--gold);padding-left:12px;}
.result-group{margin-bottom:24px;}
.result-group h4{font-size:0.85rem;font-weight:700;color:var(--gold-light);margin-bottom:10px;letter-spacing:0.05em;}
.result-list{display:flex;flex-wrap:wrap;gap:8px;}
.result-item{background:rgba(255,255,255,0.1);border:1px solid rgba(200,168,60,0.3);padding:6px 14px;border-radius:4px;font-size:0.88rem;color:var(--white);}

/* TEACHER */
#teacher{background:var(--warm-white);}
.teacher-wrap{display:grid;grid-template-columns:240px 1fr;gap:56px;align-items:start;}
.teacher-photo-wrap{width:200px;height:200px;border-radius:50% !important;overflow:hidden;border:4px solid var(--gold);box-shadow:0 8px 32px rgba(26,58,92,0.15);margin:0 auto 24px;}
.teacher-photo-wrap .img-wrap{width:100%;height:100%;}
.teacher-photo-wrap .img-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.teacher-info h3{font-family:'Noto Serif JP',serif;font-size:1.7rem;font-weight:700;color:var(--navy);margin-bottom:6px;}
.teacher-sub{color:var(--gold-dark);font-size:0.9rem;font-weight:700;margin-bottom:20px;}
.teacher-text{font-size:0.93rem;color:var(--gray);line-height:1.85;margin-bottom:20px;}
.teacher-profile{background:var(--white);border-radius:8px;padding:22px;border-left:4px solid var(--gold);}
.teacher-profile h4{font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:10px;}
.teacher-profile ul{list-style:none;display:flex;flex-direction:column;gap:6px;}
.teacher-profile li{font-size:0.87rem;color:var(--gray);display:flex;align-items:baseline;gap:8px;}
.teacher-profile li::before{content:'';display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--gold);flex-shrink:0;}

/* COURSES */
.courses{background:var(--white);}
.courses-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
.courses-img{aspect-ratio:4/3;border-radius:8px;overflow:hidden;}
.courses-img .img-wrap{width:100%;height:100%;}
.courses-img .img-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.schedule-grid{display:grid;gap:14px;}
.schedule-card{background:var(--warm-white);border-radius:8px;padding:18px 22px;border-left:4px solid var(--gold);}
.schedule-card h4{font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:6px;}
.schedule-card .price-tag{font-size:0.92rem;font-weight:700;color:var(--gold-dark);margin-bottom:6px;}
.schedule-card p{font-size:0.87rem;color:var(--gray);line-height:1.7;}
.schedule-note{font-size:0.82rem;color:var(--gray);margin-top:14px;line-height:1.7;background:var(--gray-light);padding:12px 16px;border-radius:6px;}

/* PRICE TABLE */
.price{background:var(--warm-white);}
.price-intro{font-size:0.93rem;color:var(--gray);line-height:1.8;margin-bottom:32px;}
.table-wrap{overflow-x:auto;margin-bottom:28px;}
table{width:100%;border-collapse:collapse;font-size:0.88rem;}
thead th{background:var(--navy);color:var(--white);padding:12px 10px;text-align:center;font-weight:700;font-size:0.84rem;}
thead th:first-child{text-align:left;padding-left:16px;}
tbody tr:nth-child(even){background:var(--gray-light);}
tbody tr:nth-child(odd){background:var(--white);}
tbody td{padding:11px 10px;text-align:center;color:var(--text);border-bottom:1px solid var(--gray-light);}
tbody td:first-child{text-align:left;padding-left:16px;font-weight:700;color:var(--navy);}
.price-notes{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:16px;}
.price-note-item{background:var(--white);border-radius:6px;padding:12px 16px;border-left:3px solid var(--gold);font-size:0.87rem;color:var(--gray);}

/* ACCESS */
.access{background:var(--warm-white);}
.access-wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
.access-map{aspect-ratio:4/3;border-radius:8px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.12);}
.access-map iframe{width:100%;height:100%;border:0;}
.access-info{}
.access-item{display:flex;gap:12px;margin-bottom:18px;align-items:flex-start;}
.access-icon-box{width:36px;height:36px;background:var(--navy);border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;position:relative;}
.access-icon-box::after{content:'';position:absolute;width:14px;height:14px;background:var(--gold);border-radius:2px;}
.access-text h4{font-size:0.85rem;font-weight:700;color:var(--navy);margin-bottom:2px;}
.access-text p{font-size:0.9rem;color:var(--gray);line-height:1.6;}

/* FLOW */
.flow{background:var(--white);}
.flow-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;}
.flow-step{background:var(--warm-white);border-radius:8px;padding:28px 22px;border-bottom:4px solid var(--gold);}
.flow-num{font-size:2.5rem;font-weight:900;color:var(--gray-light);line-height:1;margin-bottom:12px;}
.flow-step h4{font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:8px;}
.flow-step p{font-size:0.87rem;color:var(--gray);line-height:1.7;}

/* CTA SECTION */
.cta-section{background:linear-gradient(135deg,var(--navy-dark) 0%,var(--navy-light) 100%);padding:80px 24px;text-align:center;}
.cta-title{font-family:'Noto Serif JP',serif;font-size:clamp(1.6rem,3.5vw,2.2rem);font-weight:700;color:var(--white);margin-bottom:16px;line-height:1.35;}
.cta-title span{color:var(--gold);}
.cta-desc{color:rgba(255,255,255,0.8);font-size:0.95rem;line-height:1.8;margin-bottom:32px;}
.cta-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}

/* FOOTER */
footer{background:var(--navy-dark);color:rgba(255,255,255,0.7);padding:48px 24px 24px;}
.footer-inner{max-width:1100px;margin:0 auto;}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:48px;margin-bottom:36px;}
.footer-brand h3{font-family:'Noto Serif JP',serif;font-size:1.2rem;color:var(--white);margin-bottom:8px;}
.footer-brand h3 span{color:var(--gold);}
.footer-brand p{font-size:0.87rem;line-height:1.8;}
.footer-col h4{font-size:0.85rem;font-weight:700;color:var(--white);margin-bottom:14px;letter-spacing:0.05em;}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:8px;}
.footer-col li a{color:rgba(255,255,255,0.6);text-decoration:none;font-size:0.87rem;transition:color 0.2s;}
.footer-col li a:hover{color:var(--gold);}
.footer-bottom{border-top:1px solid rgba(255,255,255,0.12);padding-top:20px;text-align:center;font-size:0.82rem;color:rgba(255,255,255,0.4);}

/* FLOATING CTA */
.floating-cta{position:fixed;bottom:32px;right:32px;background:var(--gold);color:var(--navy-dark);padding:14px 24px;border-radius:50px;text-decoration:none;font-weight:700;font-size:0.95rem;box-shadow:0 4px 20px rgba(0,0,0,0.25);z-index:900;transition:transform 0.2s,box-shadow 0.2s;white-space:nowrap;}
.floating-cta:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(0,0,0,0.3);}

/* EDUSHIFT */
.edushift-proposal{background:#0f172a;padding:64px 24px;}
.edushift-proposal .inner{max-width:900px;margin:0 auto;text-align:center;}
.edu-logo-tag{display:inline-block;background:#3b82f6;color:#fff;font-size:0.78rem;font-weight:700;padding:3px 12px;border-radius:2px;letter-spacing:0.08em;margin-bottom:20px;}
.edu-title{font-family:'Noto Serif JP',serif;font-size:clamp(1.5rem,3vw,2.2rem);font-weight:700;color:#fff;margin-bottom:16px;line-height:1.4;}
.edu-title span{color:#60a5fa;}
.edu-desc{color:rgba(255,255,255,0.7);font-size:0.95rem;line-height:1.8;margin-bottom:40px;}
.edu-points{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:36px;}
.edu-point{background:rgba(255,255,255,0.06);border-radius:8px;padding:24px 20px;text-align:left;border:1px solid rgba(255,255,255,0.1);}
.edu-point-num{font-size:1.8rem;font-weight:900;color:#3b82f6;line-height:1;margin-bottom:10px;}
.edu-point h4{font-size:0.95rem;font-weight:700;color:#fff;margin-bottom:8px;}
.edu-point p{font-size:0.85rem;color:rgba(255,255,255,0.65);line-height:1.7;}
.edu-price-row{display:flex;align-items:center;justify-content:center;gap:20px;margin-bottom:28px;flex-wrap:wrap;}
.edu-price{font-size:2rem;font-weight:900;color:#60a5fa;}
.edu-price small{font-size:1rem;}
.edu-cta{display:inline-block;background:#3b82f6;color:#fff;padding:14px 36px;border-radius:6px;text-decoration:none;font-weight:700;font-size:1rem;transition:background 0.2s;}
.edu-cta:hover{background:#2563eb;}

/* RESPONSIVE */
@media(max-width:768px){
  nav.pc-nav{display:none;}
  .hamburger{display:flex;}
  .nav-cta{display:none;}
  .hero-content{padding:0 24px;}
  .features-grid{grid-template-columns:1fr;}
  .zz-row{grid-template-columns:1fr !important;}
  .zz-row:nth-child(odd) .zz-img,.zz-row:nth-child(even) .zz-img{order:1;}
  .zz-row:nth-child(odd) .zz-text,.zz-row:nth-child(even) .zz-text{order:2;}
  .zz-text{padding:24px 20px;}
  section{padding:60px 20px;}
  .results-wrap{grid-template-columns:1fr;}
  .teacher-wrap{grid-template-columns:1fr;}
  .courses-wrap{grid-template-columns:1fr;}
  .access-wrap{grid-template-columns:1fr;}
  .flow-steps{grid-template-columns:1fr;}
  .footer-grid{grid-template-columns:1fr;gap:28px;}
  .price-notes{grid-template-columns:1fr;}
  .edu-points{grid-template-columns:1fr;}
  .floating-cta{bottom:20px;right:16px;font-size:0.88rem;padding:12px 18px;}
  table{font-size:0.75rem;}
  thead th{padding:6px 4px;font-size:0.72rem;}
  thead th:first-child{padding-left:8px;}
  tbody td{padding:6px 4px;}
  tbody td:first-child{padding-left:8px;}
}
@media(max-width:390px){
  .hero-btns{flex-direction:column;align-items:flex-start;}
  .hero-btns a{width:100%;text-align:center;}
}"""


def img_tag(src, alt=""):
    return f'<img src="{src}" alt="{alt}" loading="lazy">'


def img_wrap(src, alt=""):
    return f"""<div class="img-wrap">{img_tag(src, alt)}<div class="img-overlay">{IMG_OVERLAY_TEXT}</div></div>"""


def zigzag_row(idx_0based, label, h3, p, img_src):
    """0-based index: odd=1st,3rd; even=2nd,4th"""
    # odd rows (1st, 3rd) → text has fade-left
    # even rows (2nd, 4th) → text has fade-right
    if idx_0based % 2 == 0:
        text_class = "fade-left"
    else:
        text_class = "fade-right"
    return f"""<div class="zz-row">
  <div class="zz-img fade-in">{img_wrap(img_src)}</div>
  <div class="zz-text {text_class}">
    <div class="zz-label">{label}</div>
    <h3>{h3}</h3>
    <p>{p}</p>
  </div>
</div>"""


def build_html(
    title,
    school_name,
    hero_tag, hero_h1, hero_sub,
    features,          # list of (name, desc)
    zigzag_rows,       # list of (label, h3, p)
    results_year, result_groups,   # groups: list of (label, [items])
    teacher_name, teacher_title, teacher_text, teacher_profile_items,
    course_cards,      # list of (name, price, desc)
    course_note,
    price_headers, price_rows, price_notes,
    address, phone, hours, map_query,
    footer_name,
    floating_cta_text,
    imgs,              # dict: hero, zz0, zz1, result, teacher, courses
    email=None,
):
    hero_src   = imgs["hero"]
    zz0_src    = imgs["zz0"]
    zz1_src    = imgs["zz1"]
    result_src = imgs["result"]
    teach_src  = imgs["teacher"]
    course_src = imgs["courses"]

    # features HTML
    feat_html = ""
    for i, (fname, fdesc) in enumerate(features):
        feat_html += f"""<div class="feature-card fade-in">
  <div class="feature-icon"></div>
  <div class="feature-num">0{i+1}</div>
  <h3>{fname}</h3>
  <p>{fdesc}</p>
</div>"""

    # zigzag HTML (3 rows)
    zz_html = ""
    for i, (zl, zh, zp) in enumerate(zigzag_rows):
        # pick image: row0→zz0_src, row1→zz1_src, row2→course_src (reuse)
        if i == 0:
            z_src = zz0_src
        elif i == 1:
            z_src = zz1_src
        else:
            z_src = course_src
        zz_html += zigzag_row(i, zl, zh, zp, z_src)

    # results
    result_groups_html = ""
    for rlabel, ritems in result_groups:
        items_html = "".join(f'<span class="result-item">{it}</span>' for it in ritems)
        result_groups_html += f"""<div class="result-group fade-in">
  <h4>{rlabel}</h4>
  <div class="result-list">{items_html}</div>
</div>"""

    # teacher profile items
    tp_html = "".join(f"<li>{item}</li>" for item in teacher_profile_items)

    # course cards
    cc_html = ""
    for cname, cprice, cdesc in course_cards:
        cc_html += f"""<div class="schedule-card fade-in">
  <h4>{cname}</h4>
  <div class="price-tag">{cprice}</div>
  <p>{cdesc}</p>
</div>"""

    # price table
    th_html = "".join(f"<th>{h}</th>" for h in price_headers)
    tr_html = ""
    for row in price_rows:
        tds = "".join(f"<td>{c}</td>" for c in row)
        tr_html += f"<tr>{tds}</tr>"
    pnotes_html = "".join(f'<div class="price-note-item">{n}</div>' for n in price_notes)

    # access
    phone_display = phone if phone else "お問い合わせフォームよりご確認ください"
    email_html = ""
    if email:
        email_html = f"""<div class="access-item">
  <div class="access-icon-box"></div>
  <div class="access-text"><h4>メール</h4><p>{email}</p></div>
</div>"""

    # map embed
    map_encoded = map_query.replace(" ", "+")
    map_embed = f'<iframe src="https://maps.google.com/maps?q={map_encoded}&output=embed" allowfullscreen loading="lazy" title="地図"></iframe>'

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>

<!-- HEADER -->
<header>
  <div class="header-inner">
    <a href="#top" class="logo">{school_name}</a>
    <nav class="pc-nav">
      <a href="#features">特徴</a>
      <a href="#about">指導方針</a>
      <a href="#results">合格実績</a>
      <a href="#teacher">講師紹介</a>
      <a href="#courses">コース</a>
      <a href="#price">料金</a>
      <a href="#access">アクセス</a>
      <a href="#contact" class="nav-cta">{floating_cta_text}</a>
    </nav>
    <button class="hamburger" id="hamburger" aria-label="メニュー">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<nav id="mobile-nav">
  <a href="#features" class="mobile-link">特徴</a>
  <a href="#about" class="mobile-link">指導方針</a>
  <a href="#results" class="mobile-link">合格実績</a>
  <a href="#teacher" class="mobile-link">講師紹介</a>
  <a href="#courses" class="mobile-link">コース</a>
  <a href="#price" class="mobile-link">料金</a>
  <a href="#access" class="mobile-link">アクセス</a>
  <a href="#contact" class="mobile-link mobile-cta-link">{floating_cta_text}</a>
</nav>

<!-- HERO -->
<section class="hero" id="top">
  <div class="hero-img">
    {img_tag(hero_src, school_name)}
  </div>
  <div class="hero-overlay"></div>
  <div class="img-overlay" style="position:absolute;bottom:0;left:0;z-index:3;">{IMG_OVERLAY_TEXT}</div>
  <div class="hero-content">
    <span class="hero-tag">{hero_tag}</span>
    <h1>{hero_h1}</h1>
    <p class="hero-sub">{hero_sub}</p>
    <div class="hero-btns">
      <a href="#contact" class="btn-primary">{floating_cta_text}</a>
      <a href="#features" class="btn-secondary">塾の特徴を見る</a>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section class="features" id="features">
  <div class="section-inner">
    <div class="section-label">FEATURES</div>
    <h2 class="section-title">選ばれる<span>3つの理由</span></h2>
    <div class="features-grid">
      {feat_html}
    </div>
  </div>
</section>

<!-- ZIGZAG / ABOUT -->
<section class="zigzag" id="about">
  {zz_html}
</section>

<!-- RESULTS -->
<section class="results" id="results">
  <div class="section-inner">
    <div class="section-label">RESULTS</div>
    <h2 class="section-title">{results_year}</h2>
    <div class="results-wrap">
      <div class="results-img fade-in">
        {img_wrap(result_src, "合格実績")}
      </div>
      <div class="results-content">
        <div class="results-year">{results_year}</div>
        {result_groups_html}
      </div>
    </div>
  </div>
</section>

<!-- TEACHER -->
<section id="teacher">
  <div class="section-inner">
    <div class="section-label">TEACHER</div>
    <h2 class="section-title">講師紹介</h2>
    <div class="teacher-wrap fade-in">
      <div>
        <div class="teacher-photo-wrap">
          {img_wrap(teach_src, teacher_name)}
        </div>
      </div>
      <div class="teacher-info">
        <h3>{teacher_name}</h3>
        <div class="teacher-sub">{teacher_title}</div>
        <p class="teacher-text">{teacher_text}</p>
        <div class="teacher-profile">
          <h4>プロフィール</h4>
          <ul>{tp_html}</ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- COURSES -->
<section class="courses" id="courses">
  <div class="section-inner">
    <div class="section-label">COURSES</div>
    <h2 class="section-title">コース・時間割</h2>
    <div class="courses-wrap">
      <div class="courses-img fade-in">
        {img_wrap(course_src, "コース")}
      </div>
      <div>
        <div class="schedule-grid">
          {cc_html}
        </div>
        <div class="schedule-note">{course_note}</div>
      </div>
    </div>
  </div>
</section>

<!-- PRICE -->
<section class="price" id="price">
  <div class="section-inner">
    <div class="section-label">PRICE</div>
    <h2 class="section-title">料金案内</h2>
    <div class="table-wrap">
      <table>
        <thead><tr>{th_html}</tr></thead>
        <tbody>{tr_html}</tbody>
      </table>
    </div>
    <div class="price-notes">{pnotes_html}</div>
  </div>
</section>

<!-- FLOW -->
<section class="flow" id="flow">
  <div class="section-inner">
    <div class="section-label">FLOW</div>
    <h2 class="section-title">入塾の流れ</h2>
    <div class="flow-steps">
      <div class="flow-step fade-in">
        <div class="flow-num">01</div>
        <h4>お問い合わせ</h4>
        <p>お電話またはメールフォームよりお気軽にご連絡ください。</p>
      </div>
      <div class="flow-step fade-in">
        <div class="flow-num">02</div>
        <h4>無料体験・面談</h4>
        <p>現在の学習状況をヒアリングし、最適なプランをご提案します。</p>
      </div>
      <div class="flow-step fade-in">
        <div class="flow-num">03</div>
        <h4>入塾・学習スタート</h4>
        <p>ご入塾手続き後、すぐに授業を開始できます。</p>
      </div>
    </div>
  </div>
</section>

<!-- ACCESS -->
<section class="access" id="access">
  <div class="section-inner">
    <div class="section-label">ACCESS</div>
    <h2 class="section-title">アクセス</h2>
    <div class="access-wrap">
      <div class="access-map">
        {map_embed}
      </div>
      <div class="access-info">
        <div class="access-item">
          <div class="access-icon-box"></div>
          <div class="access-text"><h4>住所</h4><p>{address}</p></div>
        </div>
        <div class="access-item">
          <div class="access-icon-box"></div>
          <div class="access-text"><h4>電話</h4><p>{phone_display}</p></div>
        </div>
        {email_html}
        <div class="access-item">
          <div class="access-icon-box"></div>
          <div class="access-text"><h4>営業時間</h4><p>{hours}</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section" id="contact">
  <div class="section-inner">
    <h2 class="cta-title">まずは<span>無料体験</span>から</h2>
    <p class="cta-desc">お子さまの学習についてお気軽にご相談ください。<br>体験授業・面談のお申し込みをお待ちしています。</p>
    <div class="cta-btns">
      <a href="tel:{phone}" class="btn-primary">{floating_cta_text}</a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>{footer_name}</h3>
        <p>{address}</p>
        <p style="margin-top:8px;">TEL: {phone_display}</p>
      </div>
      <div class="footer-col">
        <h4>メニュー</h4>
        <ul>
          <li><a href="#features">塾の特徴</a></li>
          <li><a href="#results">合格実績</a></li>
          <li><a href="#teacher">講師紹介</a></li>
          <li><a href="#courses">コース</a></li>
          <li><a href="#price">料金</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>お問い合わせ</h4>
        <ul>
          <li><a href="#contact">{floating_cta_text}</a></li>
          <li><a href="#access">アクセス</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 {footer_name}. All rights reserved.</p>
    </div>
  </div>
</footer>

{edushift_section(school_name)}

<!-- FLOATING CTA -->
<a href="#contact" class="floating-cta">{floating_cta_text}</a>

{JS_BLOCK}
</body>
</html>"""
    return html


# ════════════════════════════════════════════════════════════════════════
# SCHOOL DEFINITIONS
# ════════════════════════════════════════════════════════════════════════

def generate_maedajuku(imgs):
    return build_html(
        title="ならいや 前田塾 | 松阪市の個別指導塾",
        school_name="ならいや 前田塾",
        hero_tag="指導歴15年以上のプロ塾長",
        hero_h1='丁寧な指導で<span>確実に伸びる</span>、地域の学習塾',
        hero_sub="三重県松阪市・春日町の個別指導塾。指導歴15年以上の塾長・前田洋佑が少人数制クラスと個別指導で、小学生から高校生まで丁寧に指導します。",
        features=[
            ("少人数クラス指導", "中3入試特訓など少人数クラスで、仲間と切磋琢磨しながら合格を目指せます。"),
            ("個別指導（小1〜高3）", "一人ひとりの学習状況に合わせたオーダーメイドの個別指導。小学1年生から高校3年生まで対応。"),
            ("無料補習・テスト対策", "授業に加え、無料補習やテスト直前対策も実施。自習スペースも完備で放課後も勉強できます。"),
        ],
        zigzag_rows=[
            ("OUR TEACHER", "県内大手進学塾の教室長経験者が指導", "塾長・前田洋佑は、県内大手進学塾で教室長を務めた経験を持ち、指導歴15年以上。教育現場を知り尽くしたプロが、確実に成績を伸ばす指導を行います。"),
            ("COURSES", "少人数クラスから個別指導まで多彩なコース", "少人数クラス（中3入試特訓）、個別指導（小1〜高3）、ならいやクラブ（小学生算数・国語）、英会話講座と、お子さんのニーズに合わせたコースを用意しています。"),
            ("ENVIRONMENT", "無料補習・自習スペース完備で学習をサポート", "授業以外の時間も無料補習やテスト対策を実施。自習スペースも完備し、放課後も安心して勉強できる環境を提供。オンライン対応・兄弟姉妹割引もあります。"),
        ],
        results_year="主な進学実績",
        result_groups=[
            ("高校", ["松阪高校", "松阪工業高校", "相可高校", "伊勢高校"]),
            ("大学", ["三重大学", "近畿大学", "中部大学"]),
        ],
        teacher_name="前田洋佑",
        teacher_title="塾長",
        teacher_text="県内大手進学塾での教室長経験を経て、2022年3月に「ならいや 前田塾」を開校。指導歴15年以上の実績を活かし、一人ひとりの学力と目標に合わせた丁寧な指導を提供します。2025年12月には明和校もオープン。",
        teacher_profile_items=["指導歴15年以上", "県内大手進学塾教室長経験", "2022/3/26開校", "2025/12 明和校OPEN", "兄弟姉妹割引あり"],
        course_cards=[
            ("少人数クラス（中3入試特訓）", "要相談", "仲間と切磋琢磨しながら志望校合格を目指す。"),
            ("個別指導コース（小1〜高3）", "要相談", "完全オーダーメイドの個別指導。"),
            ("ならいやクラブ（小学生）", "要相談", "算数・国語を楽しく学ぶ小学生向けコース。"),
        ],
        course_note="無料補習・テスト対策あり。自習スペース完備。オンライン対応・兄弟姉妹割引。",
        price_headers=["コース", "対象", "月額料金"],
        price_rows=[
            ["少人数クラス", "中学3年生", "要相談"],
            ["個別指導", "小1〜高3", "要相談"],
            ["ならいやクラブ", "小学生", "要相談"],
            ["英会話講座", "全学年", "要相談"],
        ],
        price_notes=["無料補習あり", "兄弟姉妹割引あり", "自習スペース無料"],
        address="三重県松阪市春日町2-133（春日町バス停徒歩1分）",
        phone="0598-31-3120",
        hours="平日15:00〜22:00 / 土曜10:00〜18:00",
        map_query="松阪市春日町2 三重県",
        footer_name="ならいや 前田塾",
        floating_cta_text="無料体験を申し込む",
        imgs=imgs,
    )


def generate_cad(imgs):
    return build_html(
        title="学習塾CAD | 大阪府柏原市の個性別指導塾",
        school_name="学習塾CAD",
        hero_tag="子どもの個性を大事にする塾",
        hero_h1='その子らしさで<span>伸びる</span>、個性別指導',
        hero_sub="大阪府柏原市・堅下駅東口徒歩2分。子どもの性格・認知特性・能力に合わせた「個性別指導」で、一人ひとりの可能性を最大限に引き出します。",
        features=[
            ("個性別指導", "性格・認知特性・能力に合わせた完全オーダーメイドの指導。その子に最適な学び方で成績向上を実現します。"),
            ("1対1の個別指導", "先生と生徒が1対1で向き合う個別指導。理解が深まるまでとことん付き合います。"),
            ("地域密着・安心料金", "柏原市に根差した地域密着の塾。安心できる料金設定で、長期的な学習支援を提供します。"),
        ],
        zigzag_rows=[
            ("OUR APPROACH", "個性を活かした学びが、本当の力を育てる", "学習塾CADでは、子どもの性格・認知特性・能力を分析し、その子に最適な指導方法を選択。「この子にはこのアプローチ」という個性別指導で、確かな成果を出します。"),
            ("ONE ON ONE", "1対1だから、どんな疑問もすぐ解決", "1対1の指導スタイルで、わからないことはその場で解決。自分のペースで学習を進め、着実に実力を積み上げることができます。"),
            ("COMMUNITY", "堅下駅すぐの便利な立地", "近鉄大阪線・堅下駅東口から徒歩2分。学校帰りにそのまま立ち寄れる便利な立地です。電話・LINE・フォームで気軽にお問い合わせください。"),
        ],
        results_year="主な進学実績",
        result_groups=[
            ("高校", ["大阪府立高校各校", "私立高校"]),
            ("大学", ["大阪近辺国公立大学", "関関同立"]),
        ],
        teacher_name="塾長",
        teacher_title="学習塾CAD代表",
        teacher_text="子どもの個性を大切にした「個性別指導」を実践。性格・認知特性・能力に合わせた指導で、その子本来の力を最大限に引き出します。地域に密着した塾として、保護者の皆様と連携した学習支援を提供します。",
        teacher_profile_items=["大阪府柏原市地域密着", "個性別指導専門", "1対1完全個別指導", "堅下駅東口徒歩2分"],
        course_cards=[
            ("小学生コース", "要相談", "基礎学力の定着から中学受験対策まで。"),
            ("中学生コース", "要相談", "定期テスト対策・高校受験対策。"),
            ("高校生コース", "要相談", "大学受験対策・推薦入試サポート。"),
        ],
        course_note="個性別指導のため、料金は面談の上決定。まずはお問い合わせを。",
        price_headers=["コース", "指導形態", "月額料金"],
        price_rows=[
            ["小学生", "1対1個別", "要相談"],
            ["中学生", "1対1個別", "要相談"],
            ["高校生", "1対1個別", "要相談"],
        ],
        price_notes=["詳細は面談の上決定", "無料体験授業あり"],
        address="大阪府柏原市大県2-2-31-101（堅下駅東口徒歩2分）",
        phone="050-3576-7829",
        email="info@ec-cad.net",
        hours="平日15:00〜22:00",
        map_query="大阪府柏原市大県2",
        footer_name="学習塾CAD",
        floating_cta_text="無料体験を申し込む",
        imgs=imgs,
    )


def generate_nix(imgs):
    return build_html(
        title="進学指導塾Nix | 集団・個別ハイブリッド進学塾",
        school_name="進学指導塾Nix",
        hero_tag="創業2016年 ハイブリッド進学塾",
        hero_h1='仲間と切磋琢磨し、<span>共に成長する</span>塾',
        hero_sub="集団指導・グループ指導・個別指導のハイブリッド型進学塾。塾生全員が仲間として高め合い、学力だけでなく社会スキルも育てます。",
        features=[
            ("ハイブリッド指導", "集団・グループ・個別の3形態を組み合わせた独自のハイブリッド指導。状況に応じて最適な学習スタイルを選べます。"),
            ("仲間との切磋琢磨", "塾生全員が仲間同士で競い合い高め合う環境。競争心と連帯感が学習意欲を高めます。"),
            ("社会スキルの育成", "学力向上だけでなく、コミュニケーション能力・協調性など社会に出てから必要なスキルも育てます。"),
        ],
        zigzag_rows=[
            ("HYBRID STYLE", "集団・グループ・個別の最適な組み合わせ", "進学指導塾Nixは2016年6月の創業以来、3つの指導形態を組み合わせたハイブリッド指導を実践。一人ひとりの学力・目標・状況に合わせた最適な学習環境を提供します。"),
            ("COMMUNITY", "仲間と競い合い、共に成長する場所", "塾生全員が互いを認め合い、競い合う環境づくりを大切にしています。ライバルがいるから頑張れる。仲間がいるから挫けない。そんな塾を目指しています。"),
            ("LIFE SKILLS", "学力と社会スキルを同時に育てる", "勉強だけでなく、プレゼンテーション・ディスカッション・問題解決能力など、社会に出てから役立つスキルも育成。真の意味での「生きる力」を養います。"),
        ],
        results_year="主な進学実績",
        result_groups=[
            ("大学", ["国公立大学", "私立大学各校"]),
            ("高校", ["地域公私立高校各校"]),
        ],
        teacher_name="塾長",
        teacher_title="進学指導塾Nix代表",
        teacher_text="2016年6月の創業以来、「仲間と共に成長する塾」というコンセプトを大切にしてきました。学力向上はもちろん、社会に出てから必要な力を育てることが私たちの使命です。",
        teacher_profile_items=["創業2016年6月", "ハイブリッド指導（集団・グループ・個別）", "社会スキル育成プログラム"],
        course_cards=[
            ("集団指導コース", "要相談", "仲間と切磋琢磨しながら学ぶ集団授業。"),
            ("グループ指導コース", "要相談", "少人数グループで深く学ぶ。"),
            ("個別指導コース", "要相談", "一対一のきめ細かな個別指導。"),
        ],
        course_note="コースは自由に組み合わせ可能。詳細はお問い合わせください。",
        price_headers=["コース", "形態", "月額料金"],
        price_rows=[
            ["集団指導", "クラス制", "要相談"],
            ["グループ指導", "少人数", "要相談"],
            ["個別指導", "1対1", "要相談"],
        ],
        price_notes=["複数コース割引あり", "体験授業実施中"],
        address="お問い合わせの上ご確認ください",
        phone="お問い合わせフォームよりご確認ください",
        hours="平日15:00〜22:00",
        map_query="東京都 進学指導塾Nix",
        footer_name="進学指導塾Nix",
        floating_cta_text="無料体験を申し込む",
        imgs=imgs,
    )


def generate_azumajuku(imgs):
    return build_html(
        title="東塾 田川後藤寺校 | 福岡県田川市の個別指導塾",
        school_name="東塾 田川後藤寺校",
        hero_tag="診断テストで最適指導",
        hero_h1='「伝わる」「飽きない」授業で<span>実力を伸ばす</span>',
        hero_sub="福岡県田川市・田川後藤寺駅徒歩3分。独自診断テストで一人ひとりに最適な指導を実施。個別指導・集団学習・e-ラーニングのハイブリッドで確実な合格をサポートします。",
        features=[
            ("独自診断テスト", "入塾時の独自診断テストで学力・弱点を把握。一人ひとりに最適なカリキュラムを作成します。"),
            ("ハイブリッド指導", "個別指導・集団学習・e-ラーニングの3形態を組み合わせた充実した指導体制。"),
            ("福岡県学習支援事業参加", "福岡県の学習支援事業にも参加。地域の教育を幅広く支援しています。"),
        ],
        zigzag_rows=[
            ("DIAGNOSIS", "独自診断テストで、あなたに最適な学習プランを", "東塾独自の診断テストで学力・弱点・得意分野を分析。一人ひとりに合ったカリキュラムを設計し、効率的に成績を伸ばします。"),
            ("HYBRID", "個別・集団・e-ラーニングのハイブリッド指導", "東俊也塾長をはじめ、数学・理科社会など科目別専任講師が担当。個別指導・集団学習・e-ラーニングを組み合わせ、多角的なアプローチで実力を養います。"),
            ("FACILITY", "1階35坪・50名以上収容の充実した施設", "田川後藤寺駅徒歩3分の便利な立地。1階は35坪で50名以上収容可能な広々とした教室。2階には自習・補習スペースもあり、放課後も安心して学習できます。"),
        ],
        results_year="主な進学実績",
        result_groups=[
            ("高校", ["田川高校", "直方高校", "飯塚高校", "嘉穂高校"]),
            ("大学", ["九州大学", "福岡大学", "西南学院大学"]),
        ],
        teacher_name="東俊也",
        teacher_title="塾長",
        teacher_text="「伝わる」「飽きない」授業をモットーに、生徒が楽しみながら実力を伸ばせる環境を作っています。独自診断テストと充実した講師陣で、一人ひとりの目標達成をサポートします。",
        teacher_profile_items=["塾長 東俊也", "講師 東亮介（公立中数学）", "講師 江頭慶一郎（理科社会）", "カウンセラー 岡本ローラ", "福岡県学習支援事業参加"],
        course_cards=[
            ("小学生基礎コース", "月額10,000円（月4回）", "基礎学力の定着。算数・国語を中心に。"),
            ("小学生標準コース", "月額15,000円（月8回）", "バランスよく全科目をカバー。"),
            ("中学生コース", "月額17,000円〜（月8回）", "定期テスト・高校受験対策。"),
        ],
        course_note="中3受験コース 月額30,000円〜（月10回）。入塾金10,000円。",
        price_headers=["コース", "回数", "月額料金"],
        price_rows=[
            ["小学生基礎", "月4回", "10,000円"],
            ["小学生標準", "月8回", "15,000円"],
            ["小学生発展", "月10回", "20,000円〜"],
            ["中学生", "月8回", "17,000円〜"],
            ["中3受験", "月10回", "30,000円〜"],
        ],
        price_notes=["入塾金10,000円", "e-ラーニング込み"],
        address="福岡県田川市平松町（田川後藤寺駅徒歩3分）",
        phone="090-9654-6179",
        hours="平日15:00〜22:00 / 土曜10:00〜18:00",
        map_query="田川市平松町 福岡県",
        footer_name="東塾 田川後藤寺校",
        floating_cta_text="無料体験を申し込む",
        imgs=imgs,
    )


def generate_suzuki(imgs):
    return build_html(
        title="プロ家庭教師 鈴木雄太 | 千葉県・16年以上の指導実績",
        school_name="プロ家庭教師 鈴木雄太",
        hero_tag="16年以上 指導実績900名超",
        hero_h1='個人契約で<span>良心的な料金</span>、プロの家庭教師',
        hero_sub="千葉県野田市在住。明治大学卒・教員免許保有の家庭教師が直接指導。仲介なしの個人契約で、良心的な料金を実現。不登校・引きこもりサポートにも対応します。",
        features=[
            ("16年以上・900名超の実績", "家庭教師歴16年以上、指導実績900名超。豊富な経験から培った確かな指導力を提供します。"),
            ("個人契約で良心的料金", "仲介業者なしの個人契約だから、質の高い指導を良心的な料金で実現。透明性の高い料金体系です。"),
            ("不登校・引きこもりサポート", "不登校・引きこもりのお子さんへの支援経験も豊富。通信制高校の講師も兼業し、幅広いニーズに対応します。"),
        ],
        zigzag_rows=[
            ("EXPERIENCE", "16年以上・900名超の指導実績", "明治大学政治経済学部卒・35歳。教員免許（社会・地歴・公民）、英検準1級保有。家庭教師歴16年以上で指導実績は900名超。MARCH合格多数など確かな実績があります。"),
            ("DIRECT CONTRACT", "仲介なし個人契約で、高品質・低価格", "大手家庭教師センターのような仲介手数料がかからない個人契約スタイル。中間コストを省くことで、良心的な料金で質の高い指導を受けられます。"),
            ("SUPPORT", "不登校・引きこもりのお子さんも歓迎", "通信制高校での講師経験も活かし、学校に行きにくいお子さんへのサポートも行っています。お子さんのペースに合わせた柔軟な指導で、一緒に前向きな一歩を踏み出します。"),
        ],
        results_year="主な合格実績",
        result_groups=[
            ("大学", ["明治大学", "青山学院大学", "中央大学", "法政大学（MARCH多数）"]),
            ("高校", ["川越東高校", "開智高校", "小金高校"]),
            ("中学", ["茗溪学園中学", "芝浦工業大学柏中学"]),
        ],
        teacher_name="鈴木雄太",
        teacher_title="プロ家庭教師",
        teacher_text="明治大学政治経済学部卒業後、16年以上にわたり家庭教師として活動。現在は通信制高校の講師も兼業しながら、幅広い生徒をサポートしています。不登校・引きこもりのお子さんへの支援経験も豊富で、どんな状況でも一緒に解決策を考えます。",
        teacher_profile_items=["明治大学政治経済学部卒（35歳）", "教員免許（社会・地歴・公民）", "英検準1級", "指導実績900名超", "不登校・引きこもりサポート対応", "千葉県野田市在住"],
        course_cards=[
            ("中学受験対応コース", "要相談", "首都圏難関中学受験対策。個人に合わせたカリキュラム。"),
            ("高校受験対応コース", "要相談", "都内・埼玉・千葉の難関高校受験対策。"),
            ("大学受験対応コース", "要相談", "MARCH・難関大受験対策。英語・社会系科目が得意。"),
        ],
        course_note="不登校・引きこもりのお子さんへの対応も可能。まずはご相談ください。",
        price_headers=["コース", "対象", "料金"],
        price_rows=[
            ["家庭教師（通常）", "小中高", "要相談"],
            ["受験対策コース", "中高生", "要相談"],
            ["不登校サポート", "全学年", "要相談"],
        ],
        price_notes=["個人契約のため良心的料金", "無料体験あり"],
        address="千葉県野田市（対応エリア：千葉県・埼玉県・東京都）",
        phone="k0nan728@icloud.com",
        email="k0nan728@icloud.com",
        hours="平日・土日対応可（要相談）",
        map_query="千葉県野田市",
        footer_name="プロ家庭教師 鈴木雄太",
        floating_cta_text="無料相談・体験申込",
        imgs=imgs,
    )


# ════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════

def main():
    # Image assignments: school → [i0,i1,i2,i3,i4,i5]
    # positions: hero=i0, zigzag-row1=i1, zigzag-row2=i2, results=i3, teacher=i4, courses=i5
    assignments = {
        "maedajuku-a.html": [6, 13, 19, 8, 5, 14],
        "cad-a.html":       [9, 11, 17, 6, 0, 15],
        "nix-a.html":       [7, 12, 18, 9, 1, 16],
        "azumajuku-a.html": [10, 13, 19, 7, 2, 17],
        "suzuki-a.html":    [8, 14, 12, 10, 3, 11],
    }

    generators = {
        "maedajuku-a.html": generate_maedajuku,
        "cad-a.html":       generate_cad,
        "nix-a.html":       generate_nix,
        "azumajuku-a.html": generate_azumajuku,
        "suzuki-a.html":    generate_suzuki,
    }

    print("Loading images from b64 library...")

    for fname, indices in assignments.items():
        print(f"\n[{fname}] Loading {len(indices)} images...")
        i0, i1, i2, i3, i4, i5 = indices
        imgs = {
            "hero":    load_b64(i0),
            "zz0":     load_b64(i1),
            "zz1":     load_b64(i2),
            "result":  load_b64(i3),
            "teacher": load_b64(i4),
            "courses": load_b64(i5),
        }
        print(f"  Images loaded. Generating HTML...")
        html = generators[fname](imgs)
        out_path = os.path.join(OUT_DIR, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        size_kb = os.path.getsize(out_path) / 1024
        size_mb = size_kb / 1024
        print(f"  Written: {out_path}")
        print(f"  Size: {size_kb:.0f} KB ({size_mb:.2f} MB)")

    print("\n=== Summary ===")
    total_size = 0
    files = list(assignments.keys())
    for fname in files:
        out_path = os.path.join(OUT_DIR, fname)
        if os.path.exists(out_path):
            sz = os.path.getsize(out_path)
            total_size += sz
            sz_kb = sz / 1024
            sz_mb = sz_kb / 1024
            ok = "OK" if sz >= 200 * 1024 else "WARN: < 200KB"
            print(f"  {fname}: {sz_kb:.0f} KB ({sz_mb:.2f} MB)  [{ok}]")
        else:
            print(f"  {fname}: MISSING!")
    print(f"\nTotal: {total_size/1024/1024:.2f} MB")


if __name__ == "__main__":
    main()
