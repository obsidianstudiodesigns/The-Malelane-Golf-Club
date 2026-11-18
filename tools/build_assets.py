"""Build web images, the logo badge, favicons, the WhatsApp/social share image and the icon sprite.

Run from the project root:  python -I tools/build_assets.py
Needs Pillow and fontTools (with brotli). Raw images live in _source/ (not in git).
"""
import io
import os
import re
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_source")
OUT = os.path.join(ROOT, "assets", "img")
os.makedirs(OUT, exist_ok=True)

INK = (14, 26, 19)
BONE = (235, 230, 214)
SAGE = (159, 176, 157)
GOLD = (207, 166, 78)

# name: (source, crop as fractions l, t, r, b or None, widths)
IMAGES = {
    "hero-wide": ("gen/hero-wide.png", None, (960, 1536)),
    "hero-tall": ("gen/hero-tall.png", None, (540, 864)),
    "impala": ("gen/impala.png", None, (640, 1280)),
    "clubhouse": ("gen/clubhouse.png", None, (640, 1280)),
    "camping": ("gen/camping.png", None, (640, 1280)),
    "pool": ("gen/pool.png", None, (480, 960)),
    "cartpath": ("gen/cartpath.png", None, (480, 960)),
    "dusk": ("gen/dusk.png", None, (960, 1536)),
    "marker": ("fb/p3.jpg", (0, .06, 1, .94), (420, 591)),
}


def load(rel, crop=None):
    im = Image.open(os.path.join(SRC, rel)).convert("RGB")
    if crop:
        w, h = im.size
        l, t, r, b = crop
        im = im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))
    return im


def save_sizes(name, im, widths):
    sizes = []
    for w in widths:
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(
            os.path.join(OUT, f"{name}-{w}.webp"), "WEBP", quality=80, method=6)
        sizes.append((w, h))
    return sizes


_CACHE = {}


def font(path, size, **axes):
    key = (path, size, tuple(sorted(axes.items())))
    if key not in _CACHE:
        from fontTools.varLib.instancer import instantiateVariableFont
        f = TTFont(path)
        f.flavor = None
        axis = {a.axisTag: a for a in f["fvar"].axes}
        f = instantiateVariableFont(f, {n: axes.get(n, a.defaultValue) for n, a in axis.items()})
        buf = io.BytesIO()
        f.save(buf)
        _CACHE[key] = buf.getvalue()
    return ImageFont.truetype(io.BytesIO(_CACHE[key]), size)


BODONI = os.path.join(ROOT, "assets", "fonts", "bodoni-moda.woff2")
BODONI_I = os.path.join(ROOT, "assets", "fonts", "bodoni-moda-italic.woff2")
HANKEN = os.path.join(ROOT, "assets", "fonts", "hanken-grotesk.woff2")


def badge():
    """The club badge from Facebook (200 px), cut out of its white corners and upscaled 2x."""
    im = Image.open(os.path.join(SRC, "fb", "logo200.jpg")).convert("RGB")
    s = 4
    big = im.resize((im.width * s, im.height * s), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=3, percent=60, threshold=2))
    m = Image.new("L", big.size, 0)
    d = ImageDraw.Draw(m)
    inset = int(3.2 * s)
    d.ellipse((inset, inset, big.width - inset - 1, big.height - inset - 1), fill=255)
    big.putalpha(m)
    out = big.resize((400, 400), Image.LANCZOS)
    out.save(os.path.join(OUT, "badge-400.png"), optimize=True)
    out.resize((192, 192), Image.LANCZOS).save(os.path.join(OUT, "badge-192.png"), optimize=True)
    out.save(os.path.join(OUT, "badge-400.webp"), "WEBP", quality=90, method=6)
    out.resize((192, 192), Image.LANCZOS).save(os.path.join(OUT, "badge-192.webp"), "WEBP", quality=90, method=6)
    return out


def mark(size, logo):
    """Favicon: the badge on a deep green disc so it reads on light and dark tabs."""
    sc = 4
    s = size * sc
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    inner = logo.resize((s, s), Image.LANCZOS)
    im.alpha_composite(inner)
    return im.resize((size, size), Image.LANCZOS)


def favicons(logo):
    for n in (16, 32, 48, 96):
        mark(n, logo).save(os.path.join(ROOT, f"favicon-{n}.png"))
    mark(256, logo).save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    for n, fn in ((192, "icon-192.png"), (512, "icon-512.png")):
        mark(n, logo).save(os.path.join(ROOT, fn))
    for n, fn, pad in ((180, "apple-touch-icon.png", .08), (512, "icon-maskable-512.png", .17)):
        bg = Image.new("RGBA", (n, n), INK + (255,))
        inner = mark(int(n * (1 - 2 * pad)), logo)
        bg.alpha_composite(inner, (int(n * pad), int(n * pad)))
        bg.convert("RGB").save(os.path.join(ROOT, fn))


def og(logo):
    """WhatsApp / social preview: the golden-hour fairway, badge, name and line."""
    W, H = 1200, 630
    photo = load("gen/hero-wide.png")
    r = max(W / photo.width, H / photo.height)
    photo = photo.resize((round(photo.width * r), round(photo.height * r)), Image.LANCZOS)
    x = (photo.width - W) // 2
    y = int((photo.height - H) * .55)
    im = photo.crop((x, y, x + W, y + H)).convert("RGBA")
    im = Image.alpha_composite(im, Image.new("RGBA", (W, H), INK + (40,)))
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    for i in range(W):
        a = int(235 * max(0, 1 - i / 820) ** 1.35)
        sd.line([(i, 0), (i, H)], fill=INK + (a,))
    im = Image.alpha_composite(im, shade)
    lw = 132
    im.alpha_composite(logo.resize((lw, lw), Image.LANCZOS), (68, 64))
    d = ImageDraw.Draw(im)
    d.text((70, 246), "The Malelane", font=font(BODONI, 72, wght=500, opsz=96), fill=BONE)
    d.text((70, 326), "Golf Club", font=font(BODONI, 72, wght=500, opsz=96), fill=BONE)
    sub = font(HANKEN, 27, wght=450)
    d.text((72, 436), "Bushveld golf 2 km from Kruger's Malelane Gate.", font=sub, fill=BONE)
    d.text((72, 474), "Nine holes, eighteen tees, camping under the trees.", font=sub, fill=SAGE)
    d.text((72, 536), "013 790 0283", font=font(HANKEN, 28, wght=650), fill=GOLD)
    im.convert("RGB").save(os.path.join(OUT, "og-share.jpg"), quality=86, optimize=True, progressive=True)


def icons():
    src = os.path.join(SRC, "dl", "icons")
    out = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
    for fn in sorted(os.listdir(src)):
        body = open(os.path.join(src, fn), encoding="utf-8").read()
        inner = re.search(r"<svg[^>]*>(.*)</svg>", body, re.S).group(1)
        inner = re.sub(r"<rect width=\"256\" height=\"256\" fill=\"none\"/>", "", inner)
        out.append(f'<symbol id="i-{fn[:-4]}" viewBox="0 0 256 256" fill="currentColor">{inner}</symbol>')
    out.append("</svg>")
    open(os.path.join(ROOT, "assets", "icons.svg"), "w", encoding="utf-8").write("\n".join(out))


if __name__ == "__main__":
    lines = []
    for name, (rel, crop, widths) in IMAGES.items():
        sizes = save_sizes(name, load(rel, crop), widths)
        lines.append(f"{name}: " + ", ".join(f"{w}x{h}" for w, h in sizes))
    with open(os.path.join(SRC, "_sizes.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    logo = badge()
    favicons(logo)
    og(logo)
    icons()
    print("\n".join(lines))
