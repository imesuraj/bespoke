"""Prepare catalogue images for the static site.

Source folders are kept out of Git; the generated assets/ folders are published
to GitHub Pages. Run this script after adding source images.
"""

from hashlib import md5
from pathlib import Path

from PIL import Image, ImageOps


SOURCE = Path("catalogue_data")
ASSETS = Path("assets")
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}

# The two loose source files that are fabric swatches rather than western-wear
# references. New source images should be placed directly in the right folder.
ROOT_FABRICS = {
    "WhatsApp Image 2026-07-10 at 14.24.27 (1).jpeg",
    "WhatsApp Image 2026-07-10 at 15.09.00.jpeg",
}


def image_files(folder: Path) -> list[Path]:
    return sorted(
        (file for file in folder.iterdir() if file.suffix.lower() in IMAGE_SUFFIXES),
        key=lambda file: file.name.lower(),
    )


def export_images(files: list[Path], destination: Path, prefix: str, deduplicate: bool = False) -> int:
    """Export a numbered JPEG set, optionally skipping exact duplicate sources."""
    destination.mkdir(parents=True, exist_ok=True)
    seen_hashes = set()
    number = 1

    for source in files:
        source_hash = md5(source.read_bytes()).hexdigest()
        if deduplicate and source_hash in seen_hashes:
            continue
        seen_hashes.add(source_hash)

        target = destination / f"{prefix}_{number:02d}.jpg"
        with Image.open(source) as image:
            ImageOps.exif_transpose(image).convert("RGB").save(target, "JPEG", quality=88, optimize=True)
        number += 1

    return number - 1


root_files = image_files(SOURCE)
root_fabric_files = [file for file in root_files if file.name in ROOT_FABRICS]
root_western_files = [file for file in root_files if file.name not in ROOT_FABRICS]

western_files = image_files(SOURCE / "apparel" / "western") + root_western_files
fabric_files = image_files(SOURCE / "apparel" / "western" / "fabrics") + root_fabric_files
indian_files = image_files(SOURCE / "apparel" / "indian")
jewellery_files = image_files(SOURCE / "jewellery")

western_count = export_images(western_files, ASSETS / "apparel" / "western", "western")
fabric_count = export_images(fabric_files, ASSETS / "apparel" / "western" / "fabrics", "fabric", deduplicate=True)
indian_count = export_images(indian_files, ASSETS / "apparel" / "indian", "indian")
jewellery_count = export_images(jewellery_files, ASSETS / "jewellery", "jewellery")

print(f"Western wear: {western_count}")
print(f"Western fabrics: {fabric_count}")
print(f"Indian wear: {indian_count}")
print(f"Jewellery: {jewellery_count}")
