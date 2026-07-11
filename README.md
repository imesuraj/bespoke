# Taara's Closet

A static GitHub Pages catalogue for apparel and jewellery from **Taara's Closet**.

## Site structure

- `index.html` — home page
- `collection.html` — Apparel landing page
- `western.html` — Western wear collection
- `fabrics.html` — Fabric Edit for western wear only
- `indian.html` — Indian wear collection
- `jewellery.html` — Jewellery collection

Customers can enquire on WhatsApp at **+91 93101 07705**. For western-wear fabric enquiries, quote the displayed fabric number.

## Image workflow

Source images are kept in `catalogue_data/` and ignored by Git. The website publishes the processed image sets in `assets/`:

| Source folder | Published folder | File prefix |
| --- | --- | --- |
| `catalogue_data/apparel/western/` | `assets/apparel/western/` | `western_` |
| `catalogue_data/apparel/western/fabric/` | `assets/apparel/western/fabrics/` | `fabric_` |
| `catalogue_data/apparel/indian/` | `assets/apparel/indian/` | `indian_` |
| `catalogue_data/jewellery/` | `assets/jewellery/` | `jewellery_` |

Run the processor after adding images:

```powershell
.\.venv\Scripts\python.exe process_images.py
```

Then update the matching loop limit in `western.html`, `fabrics.html`, `indian.html`, or `jewellery.html` if the number printed by the script changes. Commit the generated `assets/` files and push to `main`.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\pip install Pillow
```

`.venv/` and `catalogue_data/` are intentionally excluded from Git.

## Deployment

Configure GitHub Pages to deploy from the `main` branch and repository root (`/`). After pushing, wait for the Pages deployment and hard-refresh (`Ctrl+F5`) if the browser shows a cached version.
