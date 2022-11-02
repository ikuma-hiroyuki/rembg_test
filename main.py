from pathlib import Path
from PIL import Image
from rembg import remove

if __name__ == "__main__":
    origin_dir = Path(__file__).parent / "origin"
    removed_dir = Path(__file__).parent / "removed"

    if not removed_dir.exists():
        removed_dir.mkdir()

    for file in origin_dir.glob("*.jpg"):
        print(f"processing: {file.stem}")
        origin_image = Image.open(file)
        removed_image = remove(origin_image)
        removed_image.save(str(removed_dir / file.stem) + ".png")

    print("Done!")
