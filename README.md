# Abigail Blankenbiller — Portfolio

A responsive graphic design and art portfolio, built from Abigail’s supplied page references and original assets. Plain HTML, CSS, and a small contact-form script; no framework, package installation, or runtime build required.

## Preview locally

```sh
python3 -m http.server 4173 --directory dist
```

Open http://localhost:4173 in a browser. Serve **`dist/`** as the website root on any static host. All links are relative, so the site also works under a GitHub Pages project path.

## Edit the portfolio

- `scripts/build.py`: page copy, project order, social profiles, shared header/footer, and HTML templates.
- `dist/styles.css`: layout, responsive breakpoints, and typography.
- `dist/contact.js`: prepares a draft in the visitor’s email app.
- `dist/images/`: optimized copies of the supplied images and original SVG logos/icons.
- `scripts/assets.json`: responsive image dimensions and ordered case-study panel segments.

After changing copy or templates, regenerate the checked-in HTML:

```sh
python3 scripts/build.py
```

The 15 portfolio pages include Home, Graphic Design, Artwork, About Me, Contact, six design case studies, and four individual artwork pages. A custom 404 page is also included.

## Typography and images

Headings and navigation use **Rift Soft**, normal style, weight **500**, through the supplied Adobe Fonts kit (`kip2ksc`). Body copy uses **Instrument Serif** through Google Fonts. Font delivery requires an internet connection; local fallback fonts are included in the CSS.

All visual assets come from Abigail’s supplied `Portfolio Files/images` folder. No images were generated. Large case-study panels are divided into sequential, seamless WebP segments for browser compatibility and lazy loading. Their visual content and order are preserved. On a case-study page, selecting a panel opens its larger version in another tab. Each project also has a native-text overview for accessibility and small screens.

The original, full-resolution source files remain on the owner’s Desktop and are not modified by this repository.

## Contact

The recipient is `arblankenbiller@gmail.com`, from the supplied Contact reference. **The static form does not send or store messages.** It validates the fields and opens an email draft, which the visitor sends using their email app. The page also provides a direct email link. Connecting a server-side form service would be a separate integration.

## Hosting

The portfolio is published with GitHub Pages at **https://arblankenbiller.github.io/abigailblankenbiller/**. The workflow in `.github/workflows/github-pages.yml` regenerates the HTML and publishes `dist/` whenever `main` changes. It can also be run manually from the Actions tab. The repository’s Pages source is **GitHub Actions**.

`.openai/hosting.json` identifies the private Sites preview and declares `dist/` as the static directory. The same `dist/` folder can be deployed to GitHub Pages, Cloudflare Pages, Netlify, or another static host without changing the site.

The original repository license is preserved in `LICENSE`.
