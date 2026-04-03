"""
Replace the Momence embed in timetable.html with a custom class calendar.

Class data is stored in a JS array at the top of the script block —
easy to extend by adding more objects to the CLASSES array.

Term 2 2026: 20 April – 22 June 2026
Classes:
  - Movement Flow – Foundations (Adults)  |  Mon 4:00–5:00 pm  |  $35
  - Kids Creative Dance (ages 6–8)        |  Tue 3:45–4:30 pm  |  $35
"""

OLD_EMBED = '''    <!-- Momence Timetable Embed -->
    <div class="timetable-container">
      <div id="ribbon-schedule"></div>
      <script
        async
        type="module"
        host_id="235744"
        teacher_ids="[362990]"
        location_ids="[201938]"
        tag_ids="[]"
        default_filter="show-all"
        locale="en"
        lock_timezone="Australia/Brisbane"
        src="https://momence.com/plugin/host-schedule/host-schedule.js"
      ></script>
    </div>'''

NEW_CALENDAR = '''    <!-- ═══════════════════════════════════════════════════════════════════
         CUSTOM CLASS CALENDAR
         To add a new class: add an object to the CLASSES array in the
         <script> block below. No other changes needed.
         ═══════════════════════════════════════════════════════════════════ -->

    <!-- Calendar CSS -->
    <style>
      /* ── Calendar container ── */
      .cal-wrap {
        margin: 2rem 0;
      }

      /* ── Term banner ── */
      .cal-term-banner {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        background: rgba(139,92,246,0.08);
        border: 1px solid rgba(139,92,246,0.25);
        border-radius: 12px;
        padding: 0.9rem 1.4rem;
        margin-bottom: 1.75rem;
        font-size: 0.9rem;
        color: #A1A1A1;
      }
      .cal-term-banner strong { color: #fff; }
      .cal-term-banner svg { flex-shrink: 0; width: 18px; height: 18px; stroke: #8B5CF6; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

      /* ── Filter tabs ── */
      .cal-filters {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
      }
      .cal-filter-btn {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(139,92,246,0.2);
        border-radius: 50px;
        color: #A1A1A1;
        cursor: pointer;
        font-family: inherit;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        padding: 0.4rem 1rem;
        transition: all 0.2s ease;
      }
      .cal-filter-btn:hover,
      .cal-filter-btn.active {
        background: rgba(139,92,246,0.18);
        border-color: rgba(139,92,246,0.6);
        color: #fff;
      }

      /* ── Day columns grid ── */
      .cal-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 0.75rem;
      }
      @media (max-width: 900px) {
        .cal-grid { grid-template-columns: repeat(4, 1fr); }
      }
      @media (max-width: 560px) {
        .cal-grid { grid-template-columns: repeat(2, 1fr); }
      }

      /* ── Day column ── */
      .cal-day {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
      }
      .cal-day-header {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 0.95rem;
        letter-spacing: 0.1em;
        color: #A1A1A1;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid rgba(139,92,246,0.15);
        text-align: center;
      }
      .cal-day--has-class .cal-day-header {
        color: #fff;
      }

      /* ── Class card ── */
      .cal-class-card {
        background: #1A1A1A;
        border: 1px solid rgba(139,92,246,0.25);
        border-radius: 12px;
        padding: 0.85rem 1rem;
        transition: border-color 0.2s ease, transform 0.2s ease;
        cursor: default;
      }
      .cal-class-card:hover {
        border-color: rgba(139,92,246,0.6);
        transform: translateY(-2px);
      }
      .cal-class-card--kids {
        border-color: rgba(245,158,11,0.3);
      }
      .cal-class-card--kids:hover {
        border-color: rgba(245,158,11,0.7);
      }
      .cal-class-card__badge {
        display: inline-block;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        border-radius: 50px;
        padding: 0.15rem 0.55rem;
        margin-bottom: 0.45rem;
      }
      .badge--adults {
        background: rgba(139,92,246,0.15);
        color: #A78BFA;
        border: 1px solid rgba(139,92,246,0.3);
      }
      .badge--kids {
        background: rgba(245,158,11,0.12);
        color: #FBBF24;
        border: 1px solid rgba(245,158,11,0.3);
      }
      .cal-class-card__name {
        font-size: 0.88rem;
        font-weight: 700;
        color: #fff;
        line-height: 1.3;
        margin-bottom: 0.3rem;
      }
      .cal-class-card__time {
        font-size: 0.78rem;
        color: #A1A1A1;
        display: flex;
        align-items: center;
        gap: 0.3rem;
        margin-bottom: 0.25rem;
      }
      .cal-class-card__time svg {
        width: 12px; height: 12px;
        stroke: currentColor; fill: none;
        stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
        flex-shrink: 0;
      }
      .cal-class-card__meta {
        font-size: 0.75rem;
        color: #6B6B6B;
        margin-top: 0.2rem;
      }
      .cal-class-card__price {
        font-size: 0.8rem;
        font-weight: 700;
        color: #8B5CF6;
        margin-top: 0.5rem;
      }

      /* ── Empty day ── */
      .cal-empty {
        text-align: center;
        padding: 1.2rem 0;
        color: rgba(161,161,161,0.25);
        font-size: 0.75rem;
        letter-spacing: 0.05em;
      }

      /* ── No results message ── */
      .cal-no-results {
        text-align: center;
        padding: 3rem 1rem;
        color: #A1A1A1;
        font-size: 0.9rem;
        display: none;
      }
    </style>

    <div class="cal-wrap" id="classCalendar">

      <!-- Term banner -->
      <div class="cal-term-banner">
        <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        <span><strong>Term 2, 2026</strong> &nbsp;|&nbsp; 20 April – 22 June 2026 &nbsp;|&nbsp; Aligned with Queensland school terms &nbsp;|&nbsp; <strong>$35 per class</strong>, billed weekly the day before</span>
      </div>

      <!-- Filter buttons -->
      <div class="cal-filters" id="calFilters">
        <button class="cal-filter-btn active" data-filter="all">All Classes</button>
        <button class="cal-filter-btn" data-filter="adults">Adults</button>
        <button class="cal-filter-btn" data-filter="kids">Kids</button>
      </div>

      <!-- Day grid (populated by JS) -->
      <div class="cal-grid" id="calGrid"></div>
      <p class="cal-no-results" id="calNoResults">No classes match the selected filter.</p>

    </div>

    <script>
    (function () {
      /* ════════════════════════════════════════════════════════════════════
         CLASS DATA — add new classes here.
         Fields:
           name      : Display name of the class
           category  : "adults" or "kids"
           day       : 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat
           timeStart : "HH:MM" 24-hour
           timeEnd   : "HH:MM" 24-hour
           ageNote   : Optional age/audience note shown in small text
           price     : Display price string
           link      : href for booking (use "#book" until live)
         ════════════════════════════════════════════════════════════════════ */
      var CLASSES = [
        {
          name:      "Movement Flow – Foundations",
          category:  "adults",
          day:       1,
          timeStart: "16:00",
          timeEnd:   "17:00",
          ageNote:   "Adults",
          price:     "$35",
          link:      "#book"
        },
        {
          name:      "Kids Creative Dance",
          category:  "kids",
          day:       2,
          timeStart: "15:45",
          timeEnd:   "16:30",
          ageNote:   "Ages 6 – 8",
          price:     "$35",
          link:      "#book"
        }
      ];

      /* ── Helpers ── */
      var DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
      var DAYS_SHORT = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];

      function fmt12(t) {
        var parts = t.split(":");
        var h = parseInt(parts[0], 10);
        var m = parts[1];
        var ampm = h >= 12 ? "pm" : "am";
        h = h % 12 || 12;
        return h + (m !== "00" ? ":" + m : "") + " " + ampm;
      }

      function renderCalendar(filter) {
        var grid = document.getElementById("calGrid");
        var noResults = document.getElementById("calNoResults");
        grid.innerHTML = "";

        var filtered = filter === "all" ? CLASSES : CLASSES.filter(function(c){ return c.category === filter; });

        if (filtered.length === 0) {
          noResults.style.display = "block";
          return;
        }
        noResults.style.display = "none";

        /* Build day columns for days that have at least one class */
        var activeDays = [];
        for (var d = 0; d < 7; d++) {
          var dayClasses = filtered.filter(function(c){ return c.day === d; });
          activeDays.push({ day: d, classes: dayClasses });
        }

        activeDays.forEach(function(col) {
          var dayDiv = document.createElement("div");
          dayDiv.className = "cal-day" + (col.classes.length > 0 ? " cal-day--has-class" : "");

          var header = document.createElement("div");
          header.className = "cal-day-header";
          header.textContent = DAYS_SHORT[col.day];
          dayDiv.appendChild(header);

          if (col.classes.length === 0) {
            var empty = document.createElement("div");
            empty.className = "cal-empty";
            empty.textContent = "—";
            dayDiv.appendChild(empty);
          } else {
            col.classes.forEach(function(cls) {
              var card = document.createElement("div");
              card.className = "cal-class-card" + (cls.category === "kids" ? " cal-class-card--kids" : "");

              var badge = document.createElement("span");
              badge.className = "cal-class-card__badge " + (cls.category === "kids" ? "badge--kids" : "badge--adults");
              badge.textContent = cls.category === "kids" ? "Kids" : "Adults";

              var name = document.createElement("div");
              name.className = "cal-class-card__name";
              name.textContent = cls.name;

              var time = document.createElement("div");
              time.className = "cal-class-card__time";
              time.innerHTML = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>' + fmt12(cls.timeStart) + " – " + fmt12(cls.timeEnd);

              var price = document.createElement("div");
              price.className = "cal-class-card__price";
              price.textContent = cls.price + " per class";

              card.appendChild(badge);
              card.appendChild(name);
              card.appendChild(time);

              if (cls.ageNote) {
                var meta = document.createElement("div");
                meta.className = "cal-class-card__meta";
                meta.textContent = cls.ageNote;
                card.appendChild(meta);
              }

              card.appendChild(price);
              dayDiv.appendChild(card);
            });
          }

          grid.appendChild(dayDiv);
        });
      }

      /* ── Filter button logic ── */
      document.getElementById("calFilters").addEventListener("click", function(e) {
        var btn = e.target.closest(".cal-filter-btn");
        if (!btn) return;
        document.querySelectorAll(".cal-filter-btn").forEach(function(b){ b.classList.remove("active"); });
        btn.classList.add("active");
        renderCalendar(btn.dataset.filter);
      });

      /* ── Initial render ── */
      renderCalendar("all");
    })();
    </script>'''

content = open('timetable.html').read()

if OLD_EMBED in content:
    content = content.replace(OLD_EMBED, NEW_CALENDAR)
    open('timetable.html', 'w').write(content)
    print("SUCCESS: Momence embed replaced with custom calendar")
else:
    print("ERROR: Old embed block not found — check whitespace")
    # Try to find partial match
    import re
    idx = content.find('Momence Timetable Embed')
    if idx != -1:
        print(f"Found marker at line {content[:idx].count(chr(10))}")
        print(repr(content[idx:idx+200]))
