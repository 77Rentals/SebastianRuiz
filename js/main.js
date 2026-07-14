(function () {
  'use strict';

  var STORAGE_KEY = 'sr_lang';

  /* ---------- Language toggle ---------- */
  function applyLang(lang) {
    document.documentElement.setAttribute('lang', lang);

    document.querySelectorAll('[data-en]').forEach(function (el) {
      var val = el.getAttribute('data-' + lang);
      if (val !== null) el.innerHTML = val;
    });

    document.querySelectorAll('[data-en-list]').forEach(function (el) {
      var raw = el.getAttribute('data-' + lang + '-list');
      if (!raw) return;
      try {
        var items = JSON.parse(raw);
        el.innerHTML = items.map(function (i) { return '<li>' + i + '</li>'; }).join('');
      } catch (e) { /* noop */ }
    });

    document.querySelectorAll('[data-href-en]').forEach(function (el) {
      var href = el.getAttribute('data-href-' + lang) || el.getAttribute('data-href-en');
      el.setAttribute('href', href);
    });

    document.querySelectorAll('.lang-option').forEach(function (opt) {
      opt.classList.toggle('active', opt.getAttribute('data-lang') === lang);
    });

    localStorage.setItem(STORAGE_KEY, lang);
  }

  var toggle = document.getElementById('langToggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var current = document.documentElement.getAttribute('lang') || 'en';
      applyLang(current === 'en' ? 'es' : 'en');
    });
  }

  var savedLang = localStorage.getItem(STORAGE_KEY) || 'en';
  applyLang(savedLang);

  /* ---------- Mobile nav ---------- */
  var hamburger = document.getElementById('hamburger');
  var navLinks = document.getElementById('navLinks');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { navLinks.classList.remove('open'); });
    });
  }

  /* ---------- Scroll reveal ---------- */
  /* ---------- Scroll progress bar ---------- */
  var progress = document.createElement('div');
  progress.className = 'scroll-progress';
  document.body.appendChild(progress);
  function updateProgress() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();

  /* ---------- Ghost year numerals on journey items ---------- */
  document.querySelectorAll('.journey-item').forEach(function (item) {
    var year = item.querySelector('.journey-year');
    if (year && !item.hasAttribute('data-ghost')) {
      var match = year.textContent.match(/\d{4}/);
      if (match) item.setAttribute('data-ghost', match[0]);
    }
  });

  /* ---------- Gold dust particles (dark sections) ---------- */
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduceMotion) {
    document.querySelectorAll('.hero, .journey-hero, .journey-cta').forEach(function (section) {
      var layer = document.createElement('div');
      layer.className = 'dust-layer';
      var count = 10;
      for (var i = 0; i < count; i++) {
        var mote = document.createElement('span');
        mote.className = 'dust-mote';
        var size = (Math.random() * 2.5 + 1.5).toFixed(1);
        var left = (Math.random() * 100).toFixed(1);
        var duration = (Math.random() * 8 + 12).toFixed(1);
        var delay = (Math.random() * -20).toFixed(1);
        var drift = (Math.random() * 60 - 30).toFixed(0);
        mote.style.left = left + '%';
        mote.style.setProperty('--mote-size', size + 'px');
        mote.style.setProperty('--mote-duration', duration + 's');
        mote.style.setProperty('--mote-delay', delay + 's');
        mote.style.setProperty('--mote-drift', drift + 'px');
        layer.appendChild(mote);
      }
      section.appendChild(layer);
    });
  }

  /* ---------- Parallax on ghost year numerals ---------- */
  var journeyItems = document.querySelectorAll('.journey-item:not(.minor)');
  if (journeyItems.length && !reduceMotion) {
    var ticking = false;
    function updateParallax() {
      var vh = window.innerHeight;
      journeyItems.forEach(function (item) {
        var rect = item.getBoundingClientRect();
        var centerOffset = (rect.top + rect.height / 2) - vh / 2;
        var shift = centerOffset * -0.08;
        item.style.setProperty('--parallax', shift.toFixed(1) + 'px');
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(updateParallax);
        ticking = true;
      }
    }, { passive: true });
    updateParallax();
  }

  /* ---------- Stagger sibling reveals ---------- */
  document.querySelectorAll('.stats-grid, .beyond-grid, .skills-grid, .contact-grid, .edu-grid').forEach(function (grid) {
    Array.prototype.forEach.call(grid.children, function (child, i) {
      child.style.setProperty('--stagger', (i * 0.09) + 's');
    });
  });

  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------- Stat counters ---------- */
  var statEls = document.querySelectorAll('.stat-number');
  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var isDecimal = target % 1 !== 0;
    var duration = 1400;
    var start = null;

    function step(ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var value = target * eased;
      el.textContent = prefix + (isDecimal ? value.toFixed(1) : Math.round(value)) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if ('IntersectionObserver' in window && statEls.length) {
    var statIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          statIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    statEls.forEach(function (el) { statIO.observe(el); });
  }

  /* ---------- Nav background on scroll ---------- */
  var nav = document.getElementById('nav');
  window.addEventListener('scroll', function () {
    if (nav) nav.style.boxShadow = window.scrollY > 20 ? '0 8px 24px rgba(0,0,0,0.25)' : 'none';
  });
})();
