"""Generate portable HTML pages. Run with Python 3; no third-party packages needed."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
ASSETS = json.loads((ROOT / 'scripts/assets.json').read_text())

PROJECTS = [
    dict(slug='12-angry-jurors', title='12 Angry Jurors Event Promotion', short='12 Angry Jurors', asset='p1', panels=5,
         description='A course project promoting Grand Canyon University’s production of 12 Angry Jurors through a cohesive set of print and promotional materials. The flyer, direct mailer, and T-shirt design capture the play’s tension, themes of justice, and emotional intensity for a student and local audience.',
         sections=['Campaign title and identity', 'Project overview, style guide, mind map, and sketches', 'Final event flyer and printed flyer mockup', 'Direct mailer front and back, with printed mockups', 'T-shirt design and final mockup']),
    dict(slug='bambu-earth', title='Bambu Earth Advertisement Series', short='Bambu Earth', asset='p2', panels=5,
         description='A course project designing print and social media advertisements for Bambu Earth, a beauty brand offering ethically produced skin-care and self-care products. The work explores a welcoming, inclusive visual identity with natural, earthy tones and a focus on informing viewers about the products.',
         sections=['Campaign title and floral imagery', 'Project overview, objectives, target audience, creative strategy, and ideation sketches', 'Style guide with existing logos, colors, typography, and floral imagery', 'Print and social media advertisement designs', 'Advertisements presented in magazine, social media, and framed print mockups']),
    dict(slug='expedia', title='Expedia Digital Media Advertising Campaign', short='Expedia', asset='p3', panels=4,
         description='A digital advertising course project for Expedia across social media platforms. The campaign uses the brand’s blue and yellow identity to communicate friendly, successful, user-friendly travel planning, convenience, and a seamless experience.',
         sections=['Campaign title, project overview, objectives, audience, and creative strategy', 'Style guide: logos, color palette, Inter typography, and sample imagery', 'Instagram advertisement designs and campaign mockup', 'Facebook and Twitter advertisement designs and campaign mockup']),
    dict(slug='welcome-to-rockville', title='Welcome to Rockville Emblem & Merchandise Design', short='Welcome to Rockville', asset='p4', panels=3,
         description='An emblem and merchandise design project for Welcome to Rockville, a rock and metal festival in Daytona Beach, Florida. The visual identity includes a logo emblem, T-shirt, and drawstring bag, using bold graphics and imagery inspired by rock music.',
         sections=['Emblem and merchandise project overview, objectives, audience, and creative strategy', 'Emblem, T-shirt, and drawstring bag sketches, followed by digital roughs', 'Final emblem, T-shirt, and drawstring bag designs with merchandise mockups']),
    dict(slug='aiga-sf', title='AIGA SF Event Web Design', short='AIGA SF Event Web Design', asset='p5', panels=1,
         description='A single-page event website design for the AIGA San Francisco Design Conference. The design uses AIGA’s existing identity and a four-column grid to help visitors learn about the conference, its speakers, and its events. The case study includes desktop, tablet, and mobile wireframes, final designs, and device mockups.',
         sections=['Project overview, desktop, tablet and mobile wireframes, final responsive designs, and device mockups']),
    dict(slug='pride-and-prejudice', title='Pride and Prejudice Book Jacket Design', short='Pride and Prejudice', asset='p6', panels=1,
         description='A personal book jacket design for Jane Austen’s Pride and Prejudice, drawing on late nineteenth-century book design with ornamental margins and florals. The symmetrical composition features Fitzwilliam Darcy and Elizabeth Bennet facing opposite directions, yet intertwined. Each element was designed and drawn by hand in Adobe Illustrator.',
         sections=['Project overview, early sketches, final cover, complete book jacket, and book mockups']),
]
ARTWORKS = [
    dict(slug='collage-3', title='Abstract Collage #3', asset='Collage_3', dimensions='5 in x 7 in', description='This collage was the third of a series using paper collected from Life Magazine’s 1996 issue “50 Most Influential Boomers,” picked up from a local antique store.', alt='Abstract paper collage with concentric white geometric shapes, black-and-white imagery, and orange and pink patterned paper.'),
    dict(slug='collage-2', title='Abstract Collage #2', asset='Collage_2', dimensions='5 in x 7 in', description='This collage was the second of a series using paper collected from Life Magazine’s 1996 issue “50 Most Influential Boomers,” picked up from a local antique store.', alt='Geometric paper collage of interlocking green, white, black, and orange triangles and squares.'),
    dict(slug='collage-1', title='Abstract Collage #1', asset='Collage_1', dimensions='5 in x 7 in', description='This collage was the first of a series using paper collected from Life Magazine’s 1996 issue “50 Most Influential Boomers,” picked up from a local antique store.', alt='Blue ocean and white paper fragments assembled into an abstract geometric collage.'),
    dict(slug='mixed-media-collage', title='Mixed Media Collage', asset='MixedMediaCollage', dimensions='9 in x 12 in', description='For this piece I used half-inch squares, cut from acrylic paint gelli prints along with pages from a vintage macrame tutorial book, to create a quilt-style geometric collage.', alt='Quilt-style mixed media collage of green acrylic gelli prints, white paper, and vintage book pages arranged in small geometric shapes.'),
]
SOCIALS = [
    ('Flickr', 'flickr.svg', 'https://www.flickr.com/photos/199262576@N02/'),
    ('LinkedIn', 'linkedin.svg', 'https://www.linkedin.com/in/abigail-blankenbiller/'),
    ('Behance', 'behance.svg', 'https://www.behance.net/blnknblr'),
]

def e(value):
    return escape(str(value), quote=True)

def picture(asset, alt, sizes, eager=False, cls=''):
    variants = ASSETS[asset]
    default = variants[min(1, len(variants)-1)]
    srcset = ', '.join(f'images/{v["src"]} {v["width"]}w' for v in variants)
    priority = ' fetchpriority="high"' if eager else ''
    return f'<img class="{e(cls)}" src="images/{default["src"]}" srcset="{srcset}" sizes="{e(sizes)}" width="{default["width"]}" height="{default["height"]}" alt="{e(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async"{priority}>'

def header(active):
    links = [('graphic-design', 'Graphic Design'), ('artwork', 'Artwork'), ('about', 'About Me'), ('contact', 'Contact')]
    nav = ''.join(f'<a href="{slug}.html"' + (' aria-current="page"' if slug == active else '') + f'>{name}</a>' for slug,name in links)
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="index.html" aria-label="Abigail Blankenbiller — home">
    <img class="brand-wordmark" src="images/wordmark.svg" width="318" height="66" alt="Abigail Blankenbiller">
  </a>
  <nav class="site-nav" aria-label="Main navigation">{nav}</nav>
</header>'''

def footer():
    return '''<footer class="site-footer">
  <a class="footer-mark" href="index.html" aria-label="Return to homepage"><img src="images/monogram.svg" width="62" height="47" alt=""></a>
  <p class="copyright">© Abigail Blankenbiller 2026</p>
</footer>'''

def page(slug, title, description, content, active='', bodyclass='', scripts=''):
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} | Abigail Blankenbiller</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#ffffff">
  <meta property="og:title" content="{e(title)} | Abigail Blankenbiller">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <link rel="icon" href="images/monogram.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://use.typekit.net" crossorigin>
  <link rel="stylesheet" href="https://use.typekit.net/kip2ksc.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  {scripts}
</head>
<body class="{e(bodyclass)}">
<div class="site-shell">
{header(active)}
<main id="main" tabindex="-1">{content}</main>
{footer()}
</div>
</body>
</html>
'''
    (DIST / f'{slug}.html').write_text(html)

def grid(items, art=False):
    cards=[]
    for i,item in enumerate(items):
        title = item['title'] if art else item['short']
        alt = item['alt'] if art else f'{title} — project cover'
        cards.append(f'''<a class="project-card" href="{item['slug']}.html" aria-label="View {e(title)}">
  {picture(item['asset'], alt, '(max-width: 640px) 100vw, (max-width: 1000px) 50vw, 33vw', eager=i<3)}
  <span class="card-title">{e(title)}</span>
</a>''')
    return '<div class="project-grid' + (' art-grid' if art else '') + '">' + '\n'.join(cards) + '</div>'

def build():
    DIST.mkdir(exist_ok=True)
    intro = 'My name is Abigail, and my passions reside in the world of art and design. I have a keen interest in crafting brand identities, logo designs, and illustrative design. I also love experimenting with various mediums and styles, and am consistently expanding my skills. Feel free to explore my work below!'
    page('index', 'Graphic Design & Art Portfolio', 'Graphic design, illustration, and mixed media artwork by Abigail Blankenbiller, a designer and artist from Lincoln, Nebraska.', f'''
<section class="intro" aria-labelledby="intro-title">
  <img class="intro-monogram" src="images/monogram.svg" width="150" height="113" alt="">
  <div class="intro-copy"><h1 id="intro-title">Graphic designer, creative enthusiast, &amp; passionate learner.</h1><p>{e(intro)}</p></div>
</section>
<section aria-labelledby="featured-title"><div class="section-heading"><h2 id="featured-title">Featured Projects</h2></div>{grid(PROJECTS)}</section>''')
    page('graphic-design', 'Graphic Design', 'Explore six graphic design projects by Abigail Blankenbiller, from advertising and event promotion to web design and book jackets.', '<h1 class="page-heading">Graphic Design</h1>' + grid(PROJECTS), active='graphic-design')
    page('artwork', 'Artwork', 'Original abstract paper collages and mixed media artwork by Abigail Blankenbiller.', '<h1 class="page-heading">Artwork</h1>' + grid(ARTWORKS, True), active='artwork')
    socials = '<div class="social-links" aria-label="Find Abigail online">' + ''.join(f'<a href="{url}" aria-label="Abigail on {name}"><img src="images/{icon}" width="68" height="68" alt="{name}"></a>' for name, icon, url in SOCIALS) + '</div>'
    page('about', 'About Me', 'Meet Abigail Blankenbiller, an artist and graphic designer from Lincoln, Nebraska.', f'''
<div class="about">
  {picture('portrait', 'Abigail Blankenbiller smiling outdoors, wearing a patterned bucket hat and a burgundy cardigan.', '(max-width: 640px) 100vw, 41vw', eager=True, cls='portrait')}
  <section class="about-copy"><h1>About Me</h1>
    <p>My name is Abigail and I’m an artist and graphic designer from Lincoln, Nebraska. As a creative, I know what it truly means to be passionate about a project. Whether I’m creating something that authentically represents a client, or diving into learning a new artistic skill, my enthusiasm to create is limitless!</p>
    <p>I’m highly proficient in Adobe programs like Photoshop, InDesign, Illustrator, and also have experience with web design and animation. I love to combine clean, minimalist visuals with illustrative elements and bold textures. Making something that represents a concept effectively while simultaneously catching eyes is my ultimate goal!</p>
    <p>If you’d like to get in touch with me, visit my <a href="contact.html">Contact page</a>!</p>
    {socials}
    <a class="button" href="index.html">Return to homepage</a>
  </section>
</div>''', active='about', bodyclass='about-page')
    page('contact', 'Contact', 'Get in touch with graphic designer and artist Abigail Blankenbiller.', '''
<section class="contact" aria-labelledby="contact-title">
  <div class="contact-intro"><h1 id="contact-title">Let’s get in touch</h1>
    <p>Send me a message below, or email me at <a href="mailto:arblankenbiller@gmail.com">arblankenbiller@gmail.com</a></p>
  </div>
  <form class="contact-form" data-contact-form>
    <label for="name">Name</label><input id="name" name="name" autocomplete="name" maxlength="120" pattern=".*\\S.*" required>
    <label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" maxlength="254" required>
    <label for="message">Message</label><textarea id="message" name="message" rows="7" maxlength="3000" required></textarea>
    <button class="button" type="submit">Compose email</button>
    <p class="form-help" data-form-status role="status">Opens your email app with your message ready to send.</p>
    <noscript><p>Please email <a href="mailto:arblankenbiller@gmail.com">arblankenbiller@gmail.com</a> directly.</p></noscript>
  </form>
</section>''', active='contact', bodyclass='contact-page', scripts='<script src="contact.js" defer></script>')
    for art in ARTWORKS:
        page(art['slug'], art['title'], art['description'], f'''
<p class="page-heading" aria-hidden="true">Artwork</p>
<article class="art-detail">
  {picture(art['asset'], art['alt'], '(max-width: 640px) 100vw, 46vw', eager=True, cls='art-detail-image')}
  <div class="art-detail-copy"><h1>{e(art['title'])}</h1><p class="dimensions">{e(art['dimensions'])}</p>
    <p>{e(art['description'])}</p><a class="button" href="artwork.html">Return to artwork</a>
  </div>
</article>''', active='artwork', bodyclass='art-detail-page')
    for index,project in enumerate(PROJECTS):
        panels=[]
        for n in range(1, project['panels']+1):
            for i,tile in enumerate(ASSETS[f'{project["asset"]}_{n}']):
                label = project['sections'][n-1] + (f' (continued, part {i+1})' if i else '')
                loading = 'eager' if n==1 and i==0 else 'lazy'
                panels.append(f'''<a class="case-panel" href="images/{tile['src']}" target="_blank" rel="noopener" aria-label="View full-size: {e(label)} (opens in a new tab)"><img src="images/{tile['small']}" srcset="images/{tile['small']} {tile['smallWidth']}w, images/{tile['src']} {tile['width']}w" sizes="92vw" width="{tile['width']}" height="{tile['height']}" loading="{loading}" decoding="async" alt="{e(label)}"></a>''')
        next_project=PROJECTS[(index+1)%len(PROJECTS)]
        content=f'''
<div class="project-toolbar"><a class="button" href="graphic-design.html">Return to graphic design</a><h1>{e(project['title'])}</h1></div>
<details class="project-notes"><summary>Read project overview</summary><p>{e(project['description'])}</p></details>
<figure class="case-study" aria-label="{e(project['title'])} case study">{''.join(panels)}<figcaption class="sr-only">{e(project['description'])} Select any image to open it at full size in a new tab.</figcaption></figure>
<div class="project-return"><a class="button" href="graphic-design.html">Return to graphic design</a><a class="next-project" href="{next_project['slug']}.html">Next: {e(next_project['short'])} →</a></div>'''
        page(project['slug'], project['title'], project['description'], content, active='graphic-design')
    page('404', 'Page Not Found', 'Return to Abigail Blankenbiller’s graphic design and art portfolio.', '<section class="contact"><h1>Page not found</h1><p>Let’s get you back to the portfolio.</p><a class="button" href="index.html">Return to homepage</a></section>')
    print('Generated 15 portfolio pages and a 404 page in dist/.')

if __name__ == '__main__':
    build()
