/**
 * UNDRGRND Movement — Shared Layout (nav + footer)
 * ================================================
 * Single source of truth for the site navigation and footer.
 *
 * Each page contains two mount points:
 *   <div id="site-nav"></div>      (near top of <body>)
 *   <div id="site-footer"></div>   (near end of <body>)
 *
 * This script injects the canonical nav + footer markup into them and wires
 * up the mobile menu, active-link highlighting and scrolled-nav behaviour.
 * To change the menu, contact details or footer, edit THIS file only.
 *
 * The nav/footer CSS already lives inline in every page's <style> block, so
 * the injected markup is styled consistently everywhere.
 */
(function () {
  'use strict';

  /* ─── Single source of truth ──────────────────────────────────────────── */
  var MENU = [
    { label: 'Home',      href: '/' },
    { label: 'Adults',    href: '/adults.html' },
    { label: 'Kids',      href: '/kids.html' },
    { label: 'Enrol',     href: '/enrol.html' },
    { label: 'About',     href: '/about.html' },
    { label: 'Learn',     href: '/learn.html' },
    { label: 'Contact',   href: '/contact.html' }
  ];

  var NAP = {
    address: 'Surfers Paradise & surrounding areas · Gold Coast',
    phoneText: '0721 402 690',
    phoneHref: 'tel:+61721402690',
    email: 'undrgrndgc@gmail.com',
    tagline: 'Foundational movement for body and mind'
  };

  var YEAR = '2026'; // bump as needed; static to avoid Date() in cached contexts

  /* ─── Helpers ─────────────────────────────────────────────────────────── */
  function isActive(href) {
    var path = window.location.pathname;
    if (href === '/') return path === '/' || path === '/index.html';
    return path.replace(/\/$/, '') === href.replace(/\/$/, '');
  }

  function menuItems(linkClass) {
    return MENU.map(function (m) {
      var active = isActive(m.href);
      var cls = linkClass + (active ? ' active' : '');
      var cur = active ? ' aria-current="page"' : '';
      return '<li class="' + linkClass.replace('__link', '__item') + '">' +
             '<a href="' + m.href + '" class="' + cls + '"' + cur + '>' + m.label + '</a></li>';
    }).join('');
  }

  /* ─── Markup ──────────────────────────────────────────────────────────── */
  function navHTML() {
    return '' +
      '<div class="nav-mobile-overlay" id="navOverlay" aria-hidden="true"></div>' +
      '<nav class="nav-mobile-menu" id="navMobileMenu" aria-label="Mobile navigation" aria-hidden="true">' +
        '<ul class="nav-mobile-menu__list" id="navMobileList">' + menuItems('nav-mobile-menu__link') + '</ul>' +
      '</nav>' +
      '<header class="site-nav" id="siteNav" role="banner">' +
        '<div class="nav-inner">' +
          '<a href="/" class="nav-logo" aria-label="UNDRGRND Movement — Home">' +
            '<img src="/images/logo/logo-header.webp" alt="UNDRGRND Movement logo — dance and yoga studio Gold Coast" width="232" height="50" style="height:50px;width:auto;display:block;" loading="eager">' +
          '</a>' +
          '<ul class="nav-menu" id="navDesktopMenu" role="list" aria-label="Main navigation">' + menuItems('nav-menu__link') + '</ul>' +
          '<button class="nav-hamburger" id="navHamburger" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="navMobileMenu">' +
            '<span class="nav-hamburger__line" aria-hidden="true"></span>' +
            '<span class="nav-hamburger__line" aria-hidden="true"></span>' +
            '<span class="nav-hamburger__line" aria-hidden="true"></span>' +
          '</button>' +
        '</div>' +
      '</header>';
  }

  function footerLinks() {
    return MENU.map(function (m) {
      return '<li class="footer-links__item"><a href="' + m.href + '">' + m.label + '</a></li>';
    }).join('');
  }

  function footerHTML() {
    return '' +
      '<footer class="site-footer" role="contentinfo" itemscope itemtype="https://schema.org/LocalBusiness">' +
        '<div class="footer-main">' +
          '<div class="footer-col footer-col--brand">' +
            '<a href="/" class="footer-brand__logo" aria-label="UNDRGRND Movement — Home">' +
              '<img src="/images/logo/logo-full.webp" alt="UNDRGRND Movement full logo — Gold Coast" width="232" height="50" style="height:50px;width:auto;display:block;" loading="lazy">' +
            '</a>' +
            '<p class="footer-brand__tagline">' + NAP.tagline + '</p>' +
          '</div>' +
          '<div class="footer-col footer-col--links">' +
            '<h3 class="footer-col__heading">Quick Links</h3>' +
            '<ul class="footer-links" role="list">' + footerLinks() + '</ul>' +
          '</div>' +
          '<div class="footer-col footer-col--contact">' +
            '<h3 class="footer-col__heading">Contact Us</h3>' +
            '<address style="font-style: normal; line-height: 1.9;">' +
              '<span itemprop="address">' + NAP.address + '</span><br>' +
              '<a href="' + NAP.phoneHref + '" itemprop="telephone">' + NAP.phoneText + '</a><br>' +
              '<a href="mailto:' + NAP.email + '" itemprop="email">' + NAP.email + '</a>' +
            '</address>' +
          '</div>' +
        '</div>' +
        '<div class="footer-bottom">' +
          '<p class="footer-bottom__copy">&copy; ' + YEAR + ' <span itemprop="name">UNDRGRND Movement</span>. All rights reserved.</p>' +
          '<nav class="footer-bottom__links" aria-label="Legal links">' +
            '<a href="/privacy-policy.html">Privacy Policy</a>' +
            '<span aria-hidden="true">|</span>' +
            '<a href="/terms-of-service.html">Terms of Service</a>' +
          '</nav>' +
          '<p class="footer-bottom__tagline">Proudly serving Surfers Paradise &amp; the wider Gold Coast</p>' +
        '</div>' +
      '</footer>';
  }

  /* ─── Behaviour wiring ────────────────────────────────────────────────── */
  function wireNav() {
    var hamburger = document.getElementById('navHamburger');
    var mobileMenu = document.getElementById('navMobileMenu');
    var overlay = document.getElementById('navOverlay');
    var siteNav = document.getElementById('siteNav');

    function openMenu() {
      hamburger.classList.add('open'); hamburger.setAttribute('aria-expanded', 'true');
      mobileMenu.classList.add('open'); mobileMenu.setAttribute('aria-hidden', 'false');
      overlay.classList.add('open'); overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
    function closeMenu() {
      hamburger.classList.remove('open'); hamburger.setAttribute('aria-expanded', 'false');
      mobileMenu.classList.remove('open'); mobileMenu.setAttribute('aria-hidden', 'true');
      overlay.classList.remove('open'); overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    if (hamburger) {
      hamburger.addEventListener('click', function () {
        hamburger.classList.contains('open') ? closeMenu() : openMenu();
      });
    }
    if (overlay) overlay.addEventListener('click', closeMenu);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && hamburger && hamburger.classList.contains('open')) {
        closeMenu(); hamburger.focus();
      }
    });
    // Close mobile menu when a link is tapped
    if (mobileMenu) {
      mobileMenu.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', closeMenu);
      });
    }

    // Scrolled state
    function onScroll() {
      if (!siteNav) return;
      siteNav.classList.toggle('scrolled', window.scrollY > 50);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ─── Mount ───────────────────────────────────────────────────────────── */
  function mount() {
    var navMount = document.getElementById('site-nav');
    var footMount = document.getElementById('site-footer');
    if (navMount) navMount.outerHTML = navHTML();
    if (footMount) footMount.outerHTML = footerHTML();
    wireNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
