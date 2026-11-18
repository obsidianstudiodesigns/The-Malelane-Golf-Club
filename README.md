# The Malelane Golf Club

Website for The Malelane Golf Club, a nine-hole, eighteen-tee bushveld course on the R570 in Malelane, Mpumalanga, 2 km from the Malelane Gate of the Kruger National Park.

Live: https://obsidianstudiodesigns.github.io/The-Malelane-Golf-Club/

- Static HTML, CSS and JavaScript with no build step, hosted on GitHub Pages from `main`.
- Content comes from the club's Facebook page (contact details, the club badge, the "More than just a game" line, the new fairway markers post and the Newcomers Golf Day flyer) and public course write-ups (9 holes with 18 tees, par 72, the R570 splitting the course 3 and 6 holes, camping, pool, restaurant).
- Photos: the 200 m marker photo is the club's own (Facebook). Every other scene is AI-generated (Figma, gpt-image) to set the mood. Swap in real photos of the course, clubhouse, pool and campsite when the club has them.
- Look: dark bushveld green with the badge's gold, Bodoni Moda for display and Hanken Grotesk for text (both self-hosted, OFL), Phosphor icons (MIT). Feel taken from Leopard Creek and Kambaku, as the client asked. Dark only by design.
- The booking form has no backend: it opens WhatsApp to 060 485 7945 with the message filled in.
- The Newcomers Golf Day block switches itself off after 29 November 2026 and shows a "follow us on Facebook for golf days" note instead. Edit the `.event` block in `index.html` for the next event.
- `tools/build_assets.py` makes the WebP images, the cut-out badge, favicons, icon sprite and the WhatsApp/social share image (`assets/img/og-share.jpg`) from the raw files in `_source/` (not in git).
- `tools/build_pages.py` makes the privacy policy, terms, 404, robots.txt, sitemap.xml and the manifest.

## To confirm with the client

- Green fees, and whether to publish them (the site currently says the office confirms fees when you book).
- Campsite rate: "from R400 a night" comes from the Newcomers Golf Day flyer.
- Opening hours of the office, clubhouse and kitchen.
- Whether the gym mentioned in an old review still exists (left off the site).
- A higher-resolution version of the club badge (the only copy available is 200 px from Facebook).
- Whether they want a custom domain (for example malgc.co.za, which their email already uses).

Designed by [Obsidian Studio Designs](https://obsidianstudiodesigns.co.za/).
