// Nav scroll border effect
const nav = document.querySelector('.nav');
if (nav) {
  const sentinel = document.createElement('div');
  sentinel.style.cssText = 'position:absolute;top:0;left:0;width:100%;height:1px;pointer-events:none';
  document.body.prepend(sentinel);
  const obs = new IntersectionObserver(([e]) => {
    nav.classList.toggle('scrolled', !e.isIntersecting);
  }, { threshold: 0 });
  obs.observe(sentinel);
}

// Scroll reveal
const revealEls = document.querySelectorAll('.stat-block, .service-card, .arch-step, .research-card, .section-header, .compare-table-wrap, .cta__copy, .cta__form-card');
revealEls.forEach(el => el.classList.add('reveal'));
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(en => {
    if (en.isIntersecting) {
      en.target.classList.add('visible');
      revealObs.unobserve(en.target);
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
revealEls.forEach(el => revealObs.observe(el));

// Mobile nav toggle
const toggle = document.querySelector('.nav__toggle');
const links = document.querySelector('.nav__links');
const cta = document.querySelector('.nav__cta');
if (toggle && links && cta) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !open);
    if (!open) {
      links.style.cssText = 'display:flex;position:absolute;top:68px;left:0;right:0;background:rgba(251,249,246,0.97);backdrop-filter:blur(14px);flex-direction:column;padding:1.5rem 1.5rem 1rem;gap:1.25rem;border-bottom:1px solid var(--border);z-index:99;';
      cta.style.cssText = 'display:flex;position:absolute;top:calc(68px + 180px);left:0;right:0;padding:0 1.5rem 1.5rem;background:rgba(251,249,246,0.97);backdrop-filter:blur(14px);z-index:99;';
    } else {
      links.style.cssText = '';
      cta.style.cssText = '';
    }
  });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', (e) => {
    const id = a.getAttribute('href');
    const target = document.querySelector(id);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
