"""
生成 520 专属二维码
用法：
  1. 先把网页部署到 GitHub Pages 等，得到可访问的网址
  2. 在 js/config.js 里填写 PAGE_URL，或直接运行：
     python generate_qr.py https://你的网址
"""

import sys
from pathlib import Path

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
except ImportError:
    print("请先安装依赖：pip install qrcode[pil]")
    sys.exit(1)


OUTPUT = Path(__file__).parent / "520_qrcode.png"


def read_url_from_config() -> str:
    config = Path(__file__).parent / "js" / "config.js"
    if not config.exists():
        return ""
    text = config.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "PAGE_URL" in line and "=" in line:
            start = line.find('"') + 1
            end = line.rfind('"')
            if start > 0 and end > start:
                return line[start:end]
    return ""


def generate(url: str) -> None:
    url = url.strip()
    if not url or "你的用户名" in url:
        print("请提供有效的网页地址！")
        print("  方式一：python generate_qr.py https://xxx.github.io/love-520/")
        print("  方式二：在 js/config.js 里修改 PAGE_URL 后直接运行本脚本")
        sys.exit(1)

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#c77d9a", back_color="#fff8f5")
    img.save(OUTPUT)
    print(f"二维码已生成：{OUTPUT}")
    print(f"链接内容：{url}")
    print("打印这张图片，或发给她扫码即可打开你的信和合照。")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else read_url_from_config()
    generate(target)
