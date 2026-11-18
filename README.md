# The Malelane Golf Club

Website for The Malelane Golf Club, a nine-hole, eighteen-tee bushveld course on the R570 in Malelane, Mpumalanga, 2 km from the Malelane Gate of the Kruger National Park.

Live: https://obsidianstudiodesigns.github.io/The-Malelane-Golf-Club/

- Static HTML, CSS and JavaScript with no build step, hosted on GitHub Pages from `main`.
- Content comes from the club's Facebook page (contact details, the club badge, the "More than just a game" line, the new fairway markers post and the Newcomers Golf Day flyer) and public course write-ups (9 holes with 18 tees, par 72, the R570 splitting the course 3 and 6 holes, camping, pool, restaurant).
- Photos: the hero, course, photo strip, banner and cart hire images are the club's own (sent on WhatsApp, 18 November 2026), and the 200 m marker photo is from their Facebook page. The clubhouse, pool and campsite tiles are still AI-generated (Figma, gpt-image) until the club sends real photos of those.
- Look: dark bushveld green with the badge's gold, Bodoni Moda for display and Hanken Grotesk for text (both self-hosted, OFL), Phosphor icons (MIT). Feel taken from Leopard Creek and Kambaku, as the client asked. Dark only by design.
- The booking form has no backend: it opens WhatsApp to 060 485 7945 with the message filled in.
- **What's on** (weekly competitions, the Thursday special, upcoming events), **Latest results** and **2027 rates** all come from the club's Facebook posts up to 18 November 2026 (rates and membership from the "2027 rates are here" flyers).
- Each upcoming event has a `data-until` date and hides itself once that date has passed. When none are left, a "follow us on Facebook" note shows instead. To add an event, copy an `<article class="event">` block in `index.html`, change the date, text and `data-until`, and add it to the JSON-LD `SportsEvent` list in the page head.
- To update results, edit the two `.card` blocks in the `#results` section (Monthly Mug and Wednesday IPS).
- `tools/build_assets.py` makes the WebP images, the cut-out badge, favicons, icon sprite and the WhatsApp/social share image (`assets/img/og-share.jpg`) from the raw files in `_source/` (not in git).
- `tools/build_pages.py` makes the privacy policy, terms, 404, robots.txt, sitemap.xml and the manifest.

## To confirm with the client

- The 2027 rates are shown now. Check whether they want the 2026 rates shown until 1 January, and whether group rates are per player (the flyer doesn't say).
- Who keeps results and events up to date, and how often (Obsidian or the club).
- Opening hours of the office, clubhouse and kitchen.
- Whether the gym mentioned in an old review still exists (left off the site).
- A higher-resolution version of the club badge (the only copy available is 200 px from Facebook).
- Whether they want a custom domain (for example malgc.co.za, which their email already uses).

Designed by [Obsidian Studio Designs](https://obsidianstudiodesigns.co.za/).
