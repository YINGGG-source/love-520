function initDaysCounter() {
  const el = document.getElementById("days-count");
  if (!el || typeof TOGETHER_SINCE === "undefined") return;

  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const start = new Date(TOGETHER_SINCE);
  start.setHours(0, 0, 0, 0);

  const diff = Math.floor((today - start) / (1000 * 60 * 60 * 24));
  const dayNumber = diff + 1; // 在一起第 N 天（含起始日当天为第 1 天）
  el.textContent = dayNumber >= 1 ? dayNumber : "—";
}

function initParticles() {
  const container = document.getElementById("particles");
  if (!container) return;

  const symbols = ["♥", "♡", "✿", "❀"];
  for (let i = 0; i < 24; i++) {
    const p = document.createElement("span");
    p.className = "particle";
    p.textContent = symbols[Math.floor(Math.random() * symbols.length)];
    p.style.left = Math.random() * 100 + "%";
    p.style.animationDuration = 8 + Math.random() * 12 + "s";
    p.style.animationDelay = Math.random() * 10 + "s";
    p.style.fontSize = 10 + Math.random() * 14 + "px";
    container.appendChild(p);
  }
}

function initGallery() {
  const grid = document.getElementById("gallery");
  if (!grid) return;

  const photos = typeof PHOTOS !== "undefined" ? PHOTOS : [];

  if (photos.length === 0) {
    grid.innerHTML =
      '<p class="gallery-empty">还没有添加照片<br>把合照放进 images 文件夹，并在 config.js 里写上文件名</p>';
    return;
  }

  const lightbox = document.createElement("div");
  lightbox.className = "lightbox";
  lightbox.innerHTML = '<span class="lightbox-close">&times;</span><img alt="我们的瞬间">';
  document.body.appendChild(lightbox);

  const lbImg = lightbox.querySelector("img");
  const close = () => lightbox.classList.remove("active");

  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox || e.target.classList.contains("lightbox-close")) close();
  });

  photos.forEach((name) => {
    const item = document.createElement("div");
    item.className = "gallery-item";
    const img = document.createElement("img");
    img.src = "images/" + name;
    img.alt = "我们的瞬间";
    img.loading = "lazy";
    img.onerror = () => {
      item.style.display = "none";
    };
    item.appendChild(img);
    item.addEventListener("click", () => {
      lbImg.src = img.src;
      lightbox.classList.add("active");
    });
    grid.appendChild(item);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initDaysCounter();
  initParticles();
  initGallery();
});
