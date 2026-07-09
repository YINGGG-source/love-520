"""打包 GitHub 上传用 zip（解压后拖进 GitHub 上传页面）"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "上传GitHub用.zip"

INCLUDE = [
    "index.html",
    "css/style.css",
    "js/config.js",
    "js/main.js",
] + [f"images/photo{i}.jpg" for i in range(1, 27)]

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
    for rel in INCLUDE:
        path = ROOT / rel
        if path.exists():
            zf.write(path, rel.replace("\\", "/"))
        else:
            print(f"缺少: {rel}")

print(f"已生成: {OUT}")
print("解压后，把 index.html、css、js、images 拖进 GitHub 上传页面。")
