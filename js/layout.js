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
    { label: 'Programs',  href: '/kids', children: [
        { label: 'Recreational Movement Programs', href: '/kids', children: [
            { label: 'The Junior Academy · 6–10',    href: '/programs/junior-academy' },
            { label: 'The Tween Exploration · 11–14', href: '/programs/tween-exploration' },
            { label: 'The Teen Elite Lab · 14–17',   href: '/programs/teen-elite-lab' }
          ] }
      ] },
    { label: 'Enrol',     href: '/enrol' },
    { label: 'About',     href: '/about' },
    { label: 'Learn',     href: '/learn' },
    { label: 'Contact',   href: '/contact' }
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
    if (href === '/') return path === '/' || path === '/index';
    return path.replace(/\/$/, '') === href.replace(/\/$/, '');
  }

  /* Desktop dropdown items — supports one level of nested flyout */
  function dropdownItems(children) {
    return children.map(function (c) {
      if (c.children && c.children.length) {
        var sub = c.children.map(function (g) {
          return '<li><a href="' + g.href + '" class="nav-subdropdown__link">' + g.label + '</a></li>';
        }).join('');
        return '<li class="nav-dropdown__item has-subdropdown">' +
               '<a href="' + c.href + '" class="nav-dropdown__link nav-dropdown__link--parent" aria-haspopup="true">' + c.label +
               ' <span class="nav-caret nav-caret--right" aria-hidden="true">&#9656;</span></a>' +
               '<ul class="nav-subdropdown" role="menu">' + sub + '</ul>' +
               '</li>';
      }
      if (c.heading) {
        return '<li class="nav-dropdown__heading"><a href="' + c.href + '">' + c.label + '</a></li>';
      }
      return '<li><a href="' + c.href + '" class="nav-dropdown__link">' + c.label + '</a></li>';
    }).join('');
  }

  /* Mobile submenu — nested groups render as heading + indented links */
  function mobileSubItems(children) {
    return children.map(function (c) {
      if (c.children && c.children.length) {
        var inner = c.children.map(function (g) {
          return '<li><a href="' + g.href + '" class="nav-mobile-submenu__link">' + g.label + '</a></li>';
        }).join('');
        return '<li class="nav-mobile-submenu__heading"><a href="' + c.href + '">' + c.label + '</a></li>' + inner;
      }
      if (c.heading) {
        return '<li class="nav-mobile-submenu__heading"><a href="' + c.href + '">' + c.label + '</a></li>';
      }
      return '<li><a href="' + c.href + '" class="nav-mobile-submenu__link">' + c.label + '</a></li>';
    }).join('');
  }

  function menuItems(linkClass) {
    var itemClass = linkClass.replace('__link', '__item');
    var isMobile  = linkClass.indexOf('mobile') > -1;

    return MENU.map(function (m) {
      var active = isActive(m.href);
      var cls = linkClass + (active ? ' active' : '');
      var cur = active ? ' aria-current="page"' : '';

      /* Items with a submenu (e.g. Kids → Recreational → classes) */
      if (m.children && m.children.length) {
        if (isMobile) {
          return '<li class="' + itemClass + '">' +
                 '<a href="' + m.href + '" class="' + cls + '"' + cur + '>' + m.label + '</a>' +
                 '<ul class="nav-mobile-submenu">' + mobileSubItems(m.children) + '</ul>' +
                 '</li>';
        }
        return '<li class="' + itemClass + ' has-dropdown">' +
               '<a href="' + m.href + '" class="' + cls + '"' + cur + ' aria-haspopup="true">' + m.label +
               ' <span class="nav-caret" aria-hidden="true">&#9662;</span></a>' +
               '<ul class="nav-dropdown" role="menu">' + dropdownItems(m.children) + '</ul>' +
               '</li>';
      }

      return '<li class="' + itemClass + '">' +
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
          '<a href="/" class="nav-logo" aria-label="UNDRGRND Movement — Integrated Movement Arts — Home">' +
            '<img src="/images/logo/logo-header-t.webp" alt="UNDRGRND Movement logo — dance and yoga studio Gold Coast" width="96" height="50" style="height:50px;width:auto;display:block;" loading="eager">' +
            '<span class="nav-logo__tagline">Integrated Movement Arts</span>' +
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
            '<a href="/" class="footer-brand__logo" aria-label="UNDRGRND Movement — Integrated Movement Arts — Home">' +
              '<img src="/images/logo/logo-full-t.webp" alt="UNDRGRND Movement full logo — Gold Coast" width="96" height="50" style="height:50px;width:auto;display:block;" loading="lazy">' +
            '</a>' +
            '<p class="footer-brand__academy">Integrated Movement Arts</p>' +
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
            '<a href="/privacy-policy">Privacy Policy</a>' +
            '<span aria-hidden="true">|</span>' +
            '<a href="/terms-of-service">Terms of Service</a>' +
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
