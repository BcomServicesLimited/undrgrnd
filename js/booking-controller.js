/**
 * UNDRGRND Movement — Term-aware Booking Controller
 * =================================================
 * Updates booking buttons + term info based on the Queensland school terms.
 *
 *   First half of the current term   → sell the REMAINING weeks of this term
 *   Second half of the current term  → sell the NEXT full term (early re-enrol)
 *   Between terms / before the first  → sell the next upcoming full term
 *   After the final term             → "Enrolments Closed"
 *
 * Timezone: Australia/Brisbane (AEST, UTC+10, no DST).
 *
 * Elements:
 *   .dance-booking-button         → href + text updated ("Enrol Now — $price")
 *   .dance-booking-button-header  → href only updated (text stays as-is)
 *   [data-booking-term]           → filled with the term / weeks info line
 *
 * Dynamic pages can call window.updateBookingButtons() after injecting markup.
 */
(function () {
  'use strict';

  // ─── STRIPE LINKS (weeks → URL + price, $35/week) ──────────────────────────
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

  // ─── TERM DATES (Queensland school terms; inclusive, Monday starts) ────────
  var TERMS = [
    { start: '2026-01-27', end: '2026-04-02', name: 'Term 1 2026' },
    { start: '2026-04-20', end: '2026-06-26', name: 'Term 2 2026' },
    { start: '2026-07-13', end: '2026-09-18', name: 'Term 3 2026' },
    { start: '2026-10-06', end: '2026-12-11', name: 'Term 4 2026' }
  ];

  // ─── HELPERS ───────────────────────────────────────────────────────────────
  function getBrisbaneToday() {
    var nowUTC = new Date();
    var brisDate = new Date(nowUTC.getTime() + (10 * 60 * 60 * 1000)); // UTC+10
    return new Date(Date.UTC(brisDate.getUTCFullYear(), brisDate.getUTCMonth(), brisDate.getUTCDate()));
  }

  function parseDate(str) {
    var p = str.split('-');
    return new Date(Date.UTC(parseInt(p[0], 10), parseInt(p[1], 10) - 1, parseInt(p[2], 10)));
  }

  function getMondayOf(date) {
    var d = new Date(date.getTime());
    var day = d.getUTCDay();              // 0=Sun … 6=Sat
    d.setUTCDate(d.getUTCDate() + (day === 0 ? -6 : 1 - day));
    return d;
  }

  var MS_WEEK = 7 * 24 * 60 * 60 * 1000;

  function getWeeksRemaining(today, termStart, termEnd) {
    if (today < termStart || today > termEnd) return null;
    var w = Math.round((getMondayOf(termEnd).getTime() - getMondayOf(today).getTime()) / MS_WEEK) + 1;
    return Math.max(1, Math.min(10, w));
  }

  function termFullWeeks(term) {
    var w = Math.round((getMondayOf(parseDate(term.end)).getTime() - getMondayOf(parseDate(term.start)).getTime()) / MS_WEEK) + 1;
    return Math.max(1, Math.min(10, w));
  }

  var MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  function fmtDate(str) { var p = str.split('-'); return parseInt(p[2], 10) + ' ' + MONTHS[parseInt(p[1], 10) - 1]; }
  function fmtRange(start, end) { return fmtDate(start) + ' – ' + fmtDate(end); }

  function pack(weeks, term, mode) {
    if (weeks == null) return null;
    weeks = Math.max(1, Math.min(10, weeks));
    var link = TERM_LINKS[weeks];
    return { weeks: weeks, price: link.price, url: link.url, termName: term.name, dates: fmtRange(term.start, term.end), mode: mode };
  }

  // ─── DECIDE WHAT TO SELL TODAY ─────────────────────────────────────────────
  function computeBooking(today) {
    for (var i = 0; i < TERMS.length; i++) {
      var start = parseDate(TERMS[i].start);
      var end   = parseDate(TERMS[i].end);
      if (today >= start && today <= end) {
        var mid = new Date(Math.round((start.getTime() + end.getTime()) / 2));
        if (today < mid) {
          return pack(getWeeksRemaining(today, start, end), TERMS[i], 'remaining');
        }
        if (i + 1 < TERMS.length) {
          return pack(termFullWeeks(TERMS[i + 1]), TERMS[i + 1], 'next');
        }
        return pack(getWeeksRemaining(today, start, end), TERMS[i], 'remaining');
      }
    }
    for (var j = 0; j < TERMS.length; j++) {
      if (today < parseDate(TERMS[j].start)) {
        return pack(termFullWeeks(TERMS[j]), TERMS[j], 'next');
      }
    }
    return null; // after the final term
  }

  function setButtonText(btn, text) {
    var nodes = Array.prototype.slice.call(btn.childNodes);
    for (var c = 0; c < nodes.length; c++) {
      if (nodes[c].nodeType === 3) btn.removeChild(nodes[c]);
    }
    btn.appendChild(document.createTextNode(text));
  }

  // ─── APPLY ─────────────────────────────────────────────────────────────────
  function run() {
    var b = computeBooking(getBrisbaneToday());

    var notes = document.querySelectorAll('[data-booking-term]');
    for (var n = 0; n < notes.length; n++) {
      if (b) {
        notes[n].textContent = (b.mode === 'remaining')
          ? b.termName + ' (' + b.dates + ') · ' + b.weeks + ' week' + (b.weeks !== 1 ? 's' : '') + ' remaining'
          : 'Now enrolling for ' + b.termName + ' (' + b.dates + ') · ' + b.weeks + ' weeks';
      } else {
        notes[n].textContent = 'Enrolments open soon for next term';
      }
    }

    var pageButtons = document.querySelectorAll('.dance-booking-button');
    for (var p = 0; p < pageButtons.length; p++) {
      var btn = pageButtons[p];
      if (b) {
        btn.href = b.url;
        btn.removeAttribute('aria-disabled');
        btn.style.pointerEvents = '';
        btn.style.opacity = '';
        setButtonText(btn, 'Enrol Now — $' + b.price);
      } else {
        btn.href = '#';
        btn.setAttribute('aria-disabled', 'true');
        btn.style.pointerEvents = 'none';
        btn.style.opacity = '0.5';
        setButtonText(btn, 'Enrolments Closed');
      }
    }

    var headerButtons = document.querySelectorAll('.dance-booking-button-header');
    for (var h = 0; h < headerButtons.length; h++) {
      var hBtn = headerButtons[h];
      if (b) {
        hBtn.href = b.url;
        hBtn.removeAttribute('aria-disabled');
        hBtn.style.pointerEvents = '';
        hBtn.style.opacity = '';
      } else {
        hBtn.href = '#';
        hBtn.setAttribute('aria-disabled', 'true');
        hBtn.style.pointerEvents = 'none';
        hBtn.style.opacity = '0.5';
      }
    }
  }

  window.updateBookingButtons = run;
  window.UNDRGRND_Booking = {
    TERMS: TERMS,
    TERM_LINKS: TERM_LINKS,
    getBrisbaneToday: getBrisbaneToday,
    computeBooking: computeBooking
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
