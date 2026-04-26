// Clock update
function updateClock() {
  const now = new Date();
  const time = now.toLocaleTimeString('en-US', { hour12: false });
  document.querySelectorAll('#clock').forEach(el => el.textContent = time);
}
setInterval(updateClock, 1000);
updateClock();

// Typewriter effect for manifesto
const typeText = document.querySelector('.typewriter');
if (typeText) {
  const html = typeText.innerHTML;
  typeText.innerHTML = '';
  let i = 0;
  let inTag = false;
  let buffer = '';

  function type() {
    if (i < html.length) {
      const char = html[i];
      if (char === '<') { inTag = true; buffer += char; }
      else if (char === '>') { inTag = false; buffer += char; typeText.innerHTML += buffer; buffer = ''; }
      else if (inTag) { buffer += char; }
      else { typeText.innerHTML += char; }
      i++;
      setTimeout(type, Math.random() * 30 + 10);
    }
  }
  setTimeout(type, 500);
}

// Scroll-triggered counter animation
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.count);
      let current = 0;
      const step = Math.ceil(target / 40);
      const timer = setInterval(() => {
        current += step;
        if (current >= target) {
          current = target;
          clearInterval(timer);
        }
        el.textContent = current;
      }, 30);
      observer.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-value').forEach(el => observer.observe(el));

// Konami code — toggles scanlines
const konami = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'];
let konamiIndex = 0;
document.addEventListener('keydown', (e) => {
  if (e.key === konami[konamiIndex]) {
    konamiIndex++;
    if (konamiIndex === konami.length) {
      const scan = document.querySelector('.scanlines');
      scan.style.opacity = scan.style.opacity === '0' ? '1' : '0';
      konamiIndex = 0;
    }
  } else {
    konamiIndex = 0;
  }
});

// Logo hover micro-interaction — subtle rotation via CSS (handled in styles.css)
