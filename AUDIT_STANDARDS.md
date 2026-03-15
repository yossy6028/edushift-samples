# AUDIT_STANDARDS.md - 監査基準

本ドキュメントは `edushift-samples` における塾HP品質監査の基準・ルールを定義します。

---

## 🚨 絶対厳禁：他塾画像の流用禁止

- 各HTMLファイルで使用する画像は、そのHTML専用に生成・用意されたもののみ使用すること
- 他の塾・他のHTMLファイル用に生成した画像を流用・コピーすることは絶対禁止
- 画像ファイル名に塾名を含める（例: josaki_hero.jpg, nakamura_staff.jpg）
- 制作完了前に必ず「この画像はこのHTML専用か」を確認する
- 違反した場合は差し戻し対象（品質Gateで即NGとなる）

---

## 監査基準 更新履歴

### v2.2 (2026-03-14) 本HP画像流用時の品質チェック追加

#### 新規チェック項目: R-IMG-REUSE（本HP画像流用品質）

**チェック対象:** 本HPから取得した画像を流用している場合

**違反条件（目視確認が必要）:**
| # | 違反内容 | 確認方法 |
|---|---------|---------|
| A | 顔・テキストの見切れ | 画像をデコードして `image` ツールで確認 |
| B | イラスト・フリー素材（いらすとや等） | 画像をデコードして `image` ツールで確認 |
| C | ヒーロー画像が文字のみ・ロゴのみ・無地 | hero セクションのsrc画像を確認 |

**修正方針:**
- A: 別の写真を探すか、クロップ位置を調整する
- B: その画像を除外し nano-banana-pro で代替生成する
- C: 教室内/建物外観写真または nano-banana-pro 生成に差替える

**検出スクリプト補足:**
```python
# ヒーロー画像がbase64でない外部URLの場合も確認
# hero / hero-img / hero-photo クラスのsrc属性を検出
import re
hero_imgs = re.findall(r'class="[^"]*hero[^"]*"[^>]*>.*?<img[^>]*src="([^"]+)"', html, re.DOTALL)
# 各imgをimageツールで目視確認する
```

---

### v2.1 (2026-03-14) SVGプレースホルダー検出基準追加

#### 新規チェック項目: R-SVG-PH (SVGプレースホルダー禁止)

**違反条件:**
- `src="data:image/svg+xml;base64,..."` 形式の img タグが存在する
- デコード後のSVGが `<rect` + `<text` を含む（= 色付き背景に文字を重ねたプレースホルダー図）

**OK条件（誤検知除外）:**
- inline SVG (`<svg>...</svg>`) がアイコン用途 (viewBox="0 0 24 24") → OK
- background CSS の SVG ノイズフィルター → OK
- img-overlay の装飾用 SVG → OK

**修正方針:**
- 対象SVGを同バッチ他塾のbase64 JPEG写真で置換する
- 重複画像使用禁止 (R24)

#### 更新された検出スクリプト例

```python
import re, base64

def check_svg_placeholder(html_content):
    issues = []
    svg_srcs = re.findall(r'src="(data:image/svg\+xml;base64,[^"]+)"', html_content)
    for s in svg_srcs:
        b64 = s.split(',',1)[1]
        dec = base64.b64decode(b64).decode('utf-8','replace')
        if '<rect' in dec and ('<text' in dec or 'fill=' in dec):
            texts = re.findall(r'<text[^>]*>([^<]+)', dec)
            issues.append(f"SVG_PH: {texts}")
    return issues
```

---

## 既存チェック項目 (参照)

| ID | 内容 |
|----|------|
| R18 | ... |
| R19 | ... |
| R20 | ... |
| R22 | ... |
| R24 | 同一画像の重複使用禁止 |
| R27 | ... |
| R30 | ... |
| R35 | ... |
| R36 | ... |
| R-SVG-PH | SVGプレースホルダー禁止 (v2.1追加) |
