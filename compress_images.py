"""批量压缩图片到适合网页的大小"""
from pathlib import Path
from PIL import Image

IMAGES_DIR = Path(__file__).parent / "images"
MAX_SIZE = 1200  # 最大边长
QUALITY = 80     # JPEG 质量

for path in sorted(IMAGES_DIR.glob("*.jpg")):
    original_size = path.stat().st_size / (1024 * 1024)
    img = Image.open(path)
    w, h = img.size

    if max(w, h) > MAX_SIZE:
        ratio = MAX_SIZE / max(w, h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)

    img.save(path, "JPEG", quality=QUALITY, optimize=True)
    new_size = path.stat().st_size / (1024 * 1024)
    print(f"{path.name}: {original_size:.1f}MB → {new_size:.1f}MB  ({w}x{h} → {img.size[0]}x{img.size[1]})")

print("\n全部压缩完成！")