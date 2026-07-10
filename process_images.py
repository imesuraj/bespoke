import os
import hashlib
from PIL import Image

# Define source and destination folders
source_dir = r'catalogue_data'
dest_dir = r'assets/images'
shades_dir = os.path.join(source_dir, 'shades')
fabrics_dir = r'assets/fabrics'

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Get catalogue images and sort them
files = sorted([f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

for i, filename in enumerate(files):
    old_path = os.path.join(source_dir, filename)

    # Generate a new name
    new_name = f"apparel_{i+1:02d}.jpg"
    new_path = os.path.join(dest_dir, new_name)

    # Process
    with Image.open(old_path) as img:
        # Check for screenshot (based on inspection, it was 09.34.36)
        if "09.34.36.jpeg" in filename:
            width, height = img.size
            img = img.crop((0, 150, width, height - 150))
            print(f"Cropped {filename}")

        img.save(new_path, "JPEG")
        print(f"Saved {new_name}")

# Export fabric options separately. Catalogue data is ignored by Git, but assets are
# published with GitHub Pages. Exact duplicate source files are excluded.
if not os.path.exists(fabrics_dir):
    os.makedirs(fabrics_dir)

seen = set()
shade_files = sorted(f for f in os.listdir(shades_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png')))
fabric_number = 1
for filename in shade_files:
    old_path = os.path.join(shades_dir, filename)
    file_hash = hashlib.md5(open(old_path, 'rb').read()).hexdigest()
    if file_hash in seen:
        continue
    seen.add(file_hash)
    new_path = os.path.join(fabrics_dir, f"fabric_{fabric_number:02d}.jpg")
    with Image.open(old_path) as img:
        img.convert('RGB').save(new_path, "JPEG", quality=88, optimize=True)
    fabric_number += 1

print(f"Saved {fabric_number - 1} unique fabric options")
