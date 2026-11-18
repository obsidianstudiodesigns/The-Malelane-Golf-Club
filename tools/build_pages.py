"""Build privacy.html, terms.html, 404.html, robots.txt, sitemap.xml and site.webmanifest.

Run from the project root:  python -I tools/build_pages.py
"""
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "The-Malelane-Golf-Club"
BASE = f"https://obsidianstudiodesigns.github.io/{REPO}/"
UPDATED = "November 2026"
NAME = "The Malelane Golf Club"


def page(slug, title, desc, body, robots="index, follow"):
    nf = slug == "404.html"
    pre = f"/{REPO}/" if nf else ""
    canon = "" if nf else f'<link rel="canonical" href="{BASE}{slug}">\n'
    return f"""<!DOCTYPE html>
<html lang="en-ZA" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
{canon}<meta name="theme-color" content="#0e1a13">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}assets/img/og-share.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<link rel="icon" href="{pre}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}favicon-32.png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<link rel="manifest" href="{pre}site.webmanifest">
{f'<base href="/{REPO}/">' if nf else ''}
<link rel="stylesheet" href="assets/css/style.css?v=3">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav nav--plain">
  <div class="nav__inner">
    <a class="brand" href="./" aria-label="{NAME}, home">
      <img src="assets/img/badge-192.webp" alt="" width="48" height="48">
      <span class="brand__name">The Malelane<br>Golf Club</span>
    </a>
    <a class="btn btn--line" href="./">Back to the club</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__bottom" style="border-top:0;padding-top:0">
      <p>&copy; {date.today().year} {NAME}</p>
      <ul class="footer__legal">
        <li><a href="privacy.html">Privacy policy</a></li>
        <li><a href="terms.html">Terms of use</a></li>
      </ul>
      <p class="credit">Designed by <a href="https://obsidianstudiodesigns.co.za/" target="_blank" rel="noopener">Obsidian Studio Designs</a></p>
    </div>
  </div>
</footer>
</body>
</html>
"""


CONTACT = ('<a href="tel:+27137900283">013 790 0283</a>, WhatsApp <a href="https://wa.me/27604857945">060 485 7945</a> '
           'or <a href="mailto:admin@malgc.co.za">admin@malgc.co.za</a>')

PRIVACY = f"""<section class="legal"><div class="wrap">
<h1>Privacy policy</h1>
<p class="updated">Protection of Personal Information Act, 2013 (POPIA). Last updated {UPDATED}.</p>

<p>{NAME} ("the club", "we", "us") runs a nine-hole golf course, clubhouse and campsite on the R570 in Malelane, Mpumalanga. This policy explains what personal information we collect when you book a round, a campsite or a golf day, or contact us, why we need it, and the rights you have under POPIA.</p>

<h2>1. Who is responsible</h2>
<p>The responsible party is {NAME}, R570, Malelane, 1320. Questions about your personal information go to the club office, which acts as our Information Officer: {CONTACT}.</p>

<h2>2. What we collect</h2>
<ul>
<li>Your name, phone or WhatsApp number and email address.</li>
<li>Booking details: the date and time you want to play or camp, the number of players, your handicap or club membership if you share it, and any cart or campsite you book.</li>
<li>For members: membership and subscription records.</li>
<li>Records of payments, invoices and competition results.</li>
</ul>
<p>This website does not take payments and does not ask for card or banking details.</p>

<h2>3. How the booking form works</h2>
<p>The booking form on this website does not store anything on a server. When you press "Send on WhatsApp", your browser opens WhatsApp with your message filled in, and nothing is sent until you send it yourself. Messages you send us on WhatsApp are also handled under WhatsApp's own privacy terms.</p>

<h2>4. Why we use it</h2>
<ul>
<li>To confirm tee times, campsite bookings and golf day entries, and to contact you about them.</li>
<li>To run competitions and keep members informed about club matters.</li>
<li>To keep the accounting and tax records the law requires.</li>
</ul>
<p>We only use your information for these purposes. We do not sell or rent it, and we will not send you marketing messages without your consent.</p>

<h2>5. Who we share it with</h2>
<p>We share your information only when we need to: with staff and committee members who handle your booking or membership, with the organiser of a golf day you enter, with service providers we rely on to run the club (such as our phone, email and accounting providers), with handicap and golf union systems if you are a member, or when the law requires it.</p>

<h2>6. How long we keep it</h2>
<p>Booking enquiries are deleted within 12 months. Membership, invoice and payment records are kept for as long as tax law requires (currently five years), then deleted.</p>

<h2>7. Keeping it safe</h2>
<p>We take reasonable steps to protect your information against loss, misuse and unauthorised access, including password-protected devices and accounts.</p>

<h2>8. This website</h2>
<p>This website does not use advertising cookies or tracking analytics, and it does not ask you to log in. It is hosted on GitHub Pages, which may keep basic technical logs (such as IP addresses) to keep the service secure. The map is provided by Google Maps, which may set its own cookies when it loads. Links to WhatsApp, Facebook, Google Maps and email open services that have their own privacy policies.</p>

<h2>9. Your rights</h2>
<p>Under POPIA you may ask what personal information we hold about you, ask us to correct or delete it, object to how we use it, and withdraw consent you have given. Contact the club office using the details above. If you are not happy with our response you may complain to the Information Regulator (South Africa) at <a href="https://inforegulator.org.za/" target="_blank" rel="noopener">inforegulator.org.za</a>.</p>

<h2>10. Changes</h2>
<p>We may update this policy from time to time. The latest version will always be on this page.</p>
</div></section>"""

TERMS = f"""<section class="legal"><div class="wrap">
<h1>Terms of use</h1>
<p class="updated">Last updated {UPDATED}.</p>

<p>These terms apply to your use of this website and to bookings with {NAME} ("the club", "we", "us"). By using the website or booking with us you accept them.</p>

<h2>1. About the information on this site</h2>
<p>We describe the course and facilities as accurately as we can, but the information here is general. Green fees, cart hire and campsite rates can change, and the office will confirm the current rate when you book. Event details are supplied by the organiser and may change. Some photographs on this website are illustrative scenes of the Lowveld and are not all of the club itself.</p>

<h2>2. Bookings</h2>
<ul>
<li>A tee time or campsite is only booked once the office has confirmed it.</li>
<li>Please let the office know as early as possible if you need to change or cancel.</li>
<li>The club may close the course, or part of it, for maintenance, weather, competitions or safety reasons.</li>
</ul>

<h2>3. On the course and at the campsite</h2>
<ul>
<li>Please follow the club's local rules, dress code and the instructions of club staff.</li>
<li>Golf carts may only be driven by adults and must stay on paths and in the areas the club allows.</li>
<li>The course is next to the bush near the Kruger National Park. Wild animals, insects and snakes may be present. Do not approach or feed animals.</li>
<li>Take care when crossing the R570 between holes.</li>
<li>Campers are responsible for their own fires, equipment and belongings, and must keep noise down at night.</li>
</ul>

<h2>4. Your safety and our responsibility</h2>
<p>Golf carries risks, including being struck by a ball. You play, camp and use the club's facilities at your own risk, and you are responsible for any damage or injury you cause to others. As far as the law allows, the club is not responsible for loss, injury or damage that is not caused by its own negligence. The club may ask visitors to sign an indemnity form. Nothing in these terms limits your rights under the Consumer Protection Act, 2008.</p>

<h2>5. Payment</h2>
<p>Green fees, cart hire and campsite fees are paid at the club office unless the office agrees otherwise.</p>

<h2>6. Website content</h2>
<p>The text, design and images on this website belong to the club or its designers and may not be copied for commercial use without permission. Links to other websites are provided for convenience; we are not responsible for their content.</p>

<h2>7. Privacy</h2>
<p>How we handle your personal information is explained in our <a href="privacy.html">privacy policy</a>.</p>

<h2>8. Law</h2>
<p>These terms are governed by the laws of the Republic of South Africa.</p>

<h2>9. Contact</h2>
<p>{NAME}, R570, Malelane, Mpumalanga. {CONTACT}.</p>
</div></section>"""

NF = """<section class="notfound"><div>
<h1>This page is out of bounds</h1>
<p>The link may be old, or the page may have moved. Everything you need is on the home page.</p>
<a class="btn btn--gold" href="./">Back to the club</a>
</div></section>"""


def main():
    out = {
        "privacy.html": page("privacy.html", f"Privacy policy | {NAME}",
                             "How The Malelane Golf Club collects, uses and protects your personal information under POPIA.", PRIVACY),
        "terms.html": page("terms.html", f"Terms of use | {NAME}",
                           "Terms for using The Malelane Golf Club website and for tee time, campsite and golf day bookings.", TERMS),
        "404.html": page("404.html", f"Page not found | {NAME}", "This page could not be found.", NF, robots="noindex"),
    }
    for fn, html in out.items():
        open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(html)

    open(os.path.join(ROOT, "robots.txt"), "w").write(
        f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {BASE}sitemap.xml\n")

    today = date.today().isoformat()
    urls = [("", "1.0", "weekly"), ("privacy.html", "0.3", "yearly"), ("terms.html", "0.3", "yearly")]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for path, pri, freq in urls:
        xml.append(f"  <url>\n    <loc>{BASE}{path}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>")
        if path == "":
            for img in ("hero-1920.webp", "og-share.jpg", "tree-stream-895.webp", "stream-1280.webp", "tee-cart-640.webp"):
                xml.append(f"    <image:image><image:loc>{BASE}assets/img/{img}</image:loc></image:image>")
        xml.append("  </url>")
    xml.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(xml) + "\n")

    manifest = {
        "name": NAME,
        "short_name": "Malelane Golf",
        "description": "Nine-hole bushveld golf course and campsite 2 km from Kruger's Malelane Gate.",
        "start_url": "./",
        "scope": "./",
        "display": "standalone",
        "background_color": "#0e1a13",
        "theme_color": "#0e1a13",
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    open(os.path.join(ROOT, "site.webmanifest"), "w").write(json.dumps(manifest, indent=2) + "\n")
    print("pages built")


if __name__ == "__main__":
    main()
