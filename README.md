# Taara's Closet

A static GitHub Pages website for **Taara's Closet**, showcasing made-to-order western wear and available fabric options.

## Pages

- `index.html` — home page and introduction to the bespoke process
- `collection.html` — apparel collection
- `fabrics.html` — **Fabric Edit**, a numbered gallery of available prints and colourways

Customers can use the WhatsApp enquiry links to contact Taara's Closet. When enquiring about a fabric, they should quote its displayed fabric number.

## Images

The live website serves images from `assets/`:

- `assets/images/` — apparel images used on the collection page
- `assets/fabrics/` — fabric images used on the Fabric Edit page

`catalogue_data/` is the local source folder and is intentionally ignored by Git. It is not published to GitHub Pages.

### Add or replace images

1. Put source apparel images in `catalogue_data/`.
2. Put source fabric images in `catalogue_data/shades/`.
3. Run the processor:

   ```powershell
   .\.venv\Scripts\python.exe process_images.py
   ```

4. Update the `garments` descriptions in `collection.html` for new apparel images.
5. If the number of generated fabric images changes, update the loop limit in `fabrics.html` (currently `70`).
6. Commit the generated `assets/images/` and `assets/fabrics/` files, then push to `main`.

> Running `process_images.py` regenerates the files in `assets/images/`. If you manually retouch an image there, copy the final version to `catalogue_data/` first, or do not run the processor again.

## Local setup

The image processor requires Python 3 and Pillow:

```powershell
python -m venv .venv
.\.venv\Scripts\pip install Pillow
```

## Deployment

Configure GitHub Pages to deploy from the `main` branch and the repository root (`/`). After pushing, allow the Pages deployment to finish, then hard-refresh the browser (`Ctrl+F5`) if an older version is cached.
