/**
 * UNDRGRND Movement — Central Link Controller
 * ============================================
 * Dynamically updates booking buttons based on weeks remaining
 * in the current Queensland school term.
 *
 * Timezone: Australia/Brisbane (AEST, UTC+10, no DST)
 *
 * Two button types:
 *   .dance-booking-button        → page buttons (href + full text updated)
 *   .dance-booking-button-header → header nav button (href only updated, text stays "BUY NOW")
 *
 * For pages that build cards dynamically (adults.html, kids.html),
 * call window.updateBookingButtons() after injecting the card HTML.
 */

(function () {
  'use strict';

  // ─── STRIPE LINKS (weeks remaining → URL + price) ──────────────────────────
  var TERM_LINKS = [
    null, // index 0 unused
    { url: 'https://buy.stripe.com/28E6oJ6NLeZggsPfCp6J20d', price: 35  },  // 1 week
    { url: 'https://buy.stripe.com/3cI4gB6NLdVc2BZ75T6J20c', price: 70  },  // 2 weeks
    { url: 'https://buy.stripe.com/aFa6oJ4FDaJ090nduh6J20b', price: 105 },  // 3 weeks
    { url: 'https://buy.stripe.com/dRm14pfkh6sK5Ob61P6J209', price: 140 },  // 4 weeks
    { url: 'https://buy.stripe.com/14A00l6NLbN4cczgGt6J20a', price: 175 },  // 5 weeks
    { url: 'https://buy.stripe.com/9B628tegdeZg6SffCp6J208', price: 210 },  // 6 weeks
    { url: 'https://buy.stripe.com/fZubJ38VTdVcfoL1Lz6J207', price: 245 },  // 7 weeks
    { url: 'https://buy.stripe.com/fZu9AV8VTcR8b8v9e16J206', price: 280 },  // 8 weeks
    { url: 'https://buy.stripe.com/3cIfZj3Bz18q0tRduh6J205', price: 315 },  // 9 weeks
    { url: 'https://buy.stripe.com/9B600lgol4kCccz0Hv6J204', price: 350 }   // 10 weeks
  ];

  // ─── TERM DATES (Queensland school terms) ──────────────────────────────────
  // Each term: { start: 'YYYY-MM-DD', end: 'YYYY-MM-DD', name: 'Term X YYYY' }
  // Dates are inclusive. Term starts on the Monday of that week.
  var TERMS = [
    { start: '2026-01-27', end: '2026-04-02',  name: 'Term 1 2026' },
    { start: '2026-04-20', end: '2026-06-26',  name: 'Term 2 2026' },
    { start: '2026-07-13', end: '2026-09-18',  name: 'Term 3 2026' },
    { start: '2026-10-06', end: '2026-12-11',  name: 'Term 4 2026' }
  ];

  // ─── HELPERS ───────────────────────────────────────────────────────────────

  /**
   * Returns today's date as a plain Date object normalised to
   * Brisbane midnight (UTC+10). No DST adjustment needed.
   */
  function getBrisbaneToday() {
    var nowUTC = new Date();
    // Brisbane is UTC+10
    var brisbaneMs = nowUTC.getTime() + (10 * 60 * 60 * 1000);
    var brisDate = new Date(brisbaneMs);
    // Return a date-only Date at UTC midnight representing Brisbane's date
    return new Date(Date.UTC(
      brisDate.getUTCFullYear(),
      brisDate.getUTCMonth(),
      brisDate.getUTCDate()
    ));
  }

  /**
   * Parse 'YYYY-MM-DD' into a UTC midnight Date.
   */
  function parseDate(str) {
    var parts = str.split('-');
    return new Date(Date.UTC(
      parseInt(parts[0], 10),
      parseInt(parts[1], 10) - 1,
      parseInt(parts[2], 10)
    ));
  }

  /**
   * Returns the Monday on or before a given date.
   */
  function getMondayOf(date) {
    var d = new Date(date.getTime());
    var day = d.getUTCDay(); // 0=Sun, 1=Mon … 6=Sat
    var diff = (day === 0) ? -6 : 1 - day;
    d.setUTCDate(d.getUTCDate() + diff);
    return d;
  }

  /**
   * Returns the number of whole weeks remaining in the term from today.
   * "Weeks remaining" = number of Mondays left including this week's Monday.
   * Rolls over each Monday.
   *
   * Returns null if today is outside any active term.
   */
  function getWeeksRemaining(today, termStart, termEnd) {
    if (today < termStart || today > termEnd) return null;

    // Find the Monday of the term's final week
    var termEndMonday = getMondayOf(termEnd);

    // Find the Monday of the current week
    var currentMonday = getMondayOf(today);

    // Weeks remaining = (termEndMonday - currentMonday) / 7 days + 1
    var msPerWeek = 7 * 24 * 60 * 60 * 1000;
    var weeksLeft = Math.round((termEndMonday.getTime() - currentMonday.getTime()) / msPerWeek) + 1;

    // Clamp between 1 and 10
    if (weeksLeft < 1) weeksLeft = 1;
    if (weeksLeft > 10) weeksLeft = 10;

    return weeksLeft;
  }

  // ─── MAIN LOGIC ────────────────────────────────────────────────────────────

  function run() {
    var today = getBrisbaneToday();
    var weeksLeft = null;
    var termName = '';

    for (var i = 0; i < TERMS.length; i++) {
      var term = TERMS[i];
      var start = parseDate(term.start);
      var end   = parseDate(term.end);
      var w = getWeeksRemaining(today, start, end);
      if (w !== null) {
        weeksLeft = w;
        termName  = term.name;
        break;
      }
    }

    // ── Update PAGE booking buttons ─────────────────────────────────────────
    var pageButtons = document.querySelectorAll('.dance-booking-button');
    for (var p = 0; p < pageButtons.length; p++) {
      var btn = pageButtons[p];
      if (weeksLeft !== null) {
        var link = TERM_LINKS[weeksLeft];
        btn.href = link.url;
        btn.removeAttribute('aria-disabled');
        btn.style.pointerEvents = '';
        btn.style.opacity = '';
        // Preserve inner SVG icon if present, update text node only
        setButtonText(btn, 'Book Now \u2014 ' + weeksLeft + ' Week' + (weeksLeft !== 1 ? 's' : '') + ' Remaining ($' + link.price + ')');
      } else {
        btn.href = '#';
        btn.setAttribute('aria-disabled', 'true');
        btn.style.pointerEvents = 'none';
        btn.style.opacity = '0.5';
        setButtonText(btn, 'Bookings Closed');
      }
    }

    // ── Update HEADER booking button ────────────────────────────────────────
    var headerButtons = document.querySelectorAll('.dance-booking-button-header');
    for (var h = 0; h < headerButtons.length; h++) {
      var hBtn = headerButtons[h];
      if (weeksLeft !== null) {
        hBtn.href = TERM_LINKS[weeksLeft].url;
        hBtn.removeAttribute('aria-disabled');
        hBtn.style.pointerEvents = '';
        hBtn.style.opacity = '';
      } else {
        hBtn.href = '#';
        hBtn.setAttribute('aria-disabled', 'true');
        hBtn.style.pointerEvents = 'none';
        hBtn.style.opacity = '0.5';
      }
      // Header button text is never changed — stays "BUY NOW"
    }
  }

  /**
   * Updates the visible text of a button while preserving any child SVG icons.
   */
  function setButtonText(btn, text) {
    // Remove existing text nodes, keep SVG children
    var children = Array.prototype.slice.call(btn.childNodes);
    for (var c = 0; c < children.length; c++) {
      if (children[c].nodeType === 3) { // TEXT_NODE
        btn.removeChild(children[c]);
      }
    }
    // Append new text node at the end
    btn.appendChild(document.createTextNode(text));
  }

  // ── Expose globally so dynamic pages (adults.html, kids.html) can call
  //    window.updateBookingButtons() after injecting card HTML ───────────────
  window.updateBookingButtons = run;

  // ── Expose term data + helpers so other pages (e.g. timetable.html) can
  //    build term-aware UI without duplicating the pricing tables. Single
  //    source of truth stays in this file. ──────────────────────────────────
  window.UNDRGRND_Booking = {
    TERMS: TERMS,
    TERM_LINKS: TERM_LINKS,
    getBrisbaneToday: getBrisbaneToday,
    parseDate: parseDate,
    getWeeksRemaining: getWeeksRemaining
  };

  // Run after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }

})();
