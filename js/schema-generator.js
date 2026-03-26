/**
 * UNDRGRND Movement — Schema Generator
 * File: /js/schema-generator.js
 *
 * Generates JSON-LD structured data script tags for insertion into <head>.
 * All business data is sourced from site-config.json via loadSiteConfig().
 *
 * Functions:
 *   loadSiteConfig()                    — Fetches and caches site-config.json
 *   generateLocalBusinessSchema()       — LocalBusiness + DanceSchool + YogaStudio
 *   generateBreadcrumbSchema(items)     — BreadcrumbList
 *   generateServiceSchema(program)      — Service with Offer pricing
 *   generateFAQSchema(faqs)             — FAQPage
 *
 * Usage (in page <head> or top of <body>):
 *
 *   <script src="/js/schema-generator.js"></script>
 *   <script>
 *     generateLocalBusinessSchema().then(function(tag) {
 *       document.head.insertAdjacentHTML('beforeend', tag);
 *     });
 *
 *     var breadcrumbs = [
 *       { name: 'Home', url: 'https://www.undrgrnd.com.au/' },
 *       { name: 'Adults', url: 'https://www.undrgrnd.com.au/adults.html' }
 *     ];
 *     document.head.insertAdjacentHTML('beforeend', generateBreadcrumbSchema(breadcrumbs));
 *   </script>
 */

'use strict';

/* ==========================================================================
   HELPER: loadSiteConfig()
   Fetches /site-config.json and returns a Promise resolving to the parsed
   config object. Results are cached so the file is only fetched once.
   ========================================================================== */

var _siteConfigCache = null;

/**
 * Loads and caches site-config.json.
 * @returns {Promise<Object>} Parsed site-config.json object
 */
function loadSiteConfig() {
  if (_siteConfigCache) {
    return Promise.resolve(_siteConfigCache);
  }

  return fetch('/site-config.json')
    .then(function (res) {
      if (!res.ok) {
        throw new Error('schema-generator: Failed to fetch site-config.json — HTTP ' + res.status);
      }
      return res.json();
    })
    .then(function (config) {
      _siteConfigCache = config;
      return config;
    })
    .catch(function (err) {
      console.error('schema-generator: loadSiteConfig error —', err.message);
      throw err;
    });
}


/* ==========================================================================
   HELPER: buildScriptTag(schemaObject)
   Wraps a schema object in a <script type="application/ld+json"> tag string.
   ========================================================================== */

/**
 * Wraps a plain schema object in a JSON-LD script tag string.
 * @param {Object} schemaObject — Plain JS object conforming to schema.org spec
 * @returns {string} Complete <script type="application/ld+json"> tag
 */
function buildScriptTag(schemaObject) {
  return '<script type="application/ld+json">\n' +
    JSON.stringify(schemaObject, null, 2) +
    '\n</script>';
}


/* ==========================================================================
   HELPER: formatOpeningHours(hours)
   Converts site-config.json business.hours object to schema.org
   openingHours array format: ["Mo-Fr 06:00-21:00", "Sa-Su 08:00-16:00"]
   ========================================================================== */

/**
 * Converts site-config hours object to schema.org openingHours strings.
 * @param {Object} hours — site-config.json business.hours
 * @returns {string[]} Array of schema.org openingHours strings
 */
function formatOpeningHours(hours) {
  if (!hours) return [];

  /* Map day names to schema.org two-letter codes */
  var dayMap = {
    monday:    'Mo',
    tuesday:   'Tu',
    wednesday: 'We',
    thursday:  'Th',
    friday:    'Fr',
    saturday:  'Sa',
    sunday:    'Su'
  };

  /**
   * Convert "6:00 AM - 9:00 PM" → "06:00-21:00"
   * @param {string} timeRange
   * @returns {string}
   */
  function convertTimeRange(timeRange) {
    if (!timeRange || timeRange === 'Closed') return null;

    var parts = timeRange.split(/\s*[-–]\s*/);
    if (parts.length !== 2) return null;

    function to24h(t) {
      var match = t.trim().match(/^(\d{1,2}):(\d{2})\s*(AM|PM)$/i);
      if (!match) return null;
      var h = parseInt(match[1], 10);
      var m = match[2];
      var period = match[3].toUpperCase();
      if (period === 'PM' && h !== 12) h += 12;
      if (period === 'AM' && h === 12) h = 0;
      return (h < 10 ? '0' : '') + h + ':' + m;
    }

    var start = to24h(parts[0]);
    var end   = to24h(parts[1]);
    if (!start || !end) return null;
    return start + '-' + end;
  }

  /* Group consecutive days with identical hours */
  var dayOrder = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
  var groups = [];
  var i = 0;

  while (i < dayOrder.length) {
    var day = dayOrder[i];
    if (!hours[day] || hours[day] === 'Closed') { i++; continue; }

    var timeRange = convertTimeRange(hours[day]);
    if (!timeRange) { i++; continue; }

    /* Look ahead for consecutive days with the same hours */
    var groupStart = i;
    var j = i + 1;
    while (j < dayOrder.length && hours[dayOrder[j]] && convertTimeRange(hours[dayOrder[j]]) === timeRange) {
      j++;
    }

    var startCode = dayMap[dayOrder[groupStart]];
    var endCode   = dayMap[dayOrder[j - 1]];

    if (groupStart === j - 1) {
      groups.push(startCode + ' ' + timeRange);
    } else {
      groups.push(startCode + '-' + endCode + ' ' + timeRange);
    }

    i = j;
  }

  return groups;
}


/* ==========================================================================
   1. generateLocalBusinessSchema()
   Schema types: LocalBusiness + DanceSchool + YogaStudio
   Data source: site-config.json → business, project, seo
   ========================================================================== */

/**
 * Generates a LocalBusiness + DanceSchool + YogaStudio JSON-LD schema tag.
 * Pulls all data from site-config.json.
 *
 * @returns {Promise<string>} Promise resolving to <script> tag string
 */
function generateLocalBusinessSchema() {
  return loadSiteConfig().then(function (config) {
    var business = config.business;
    var project  = config.project;
    var seo      = config.seo;

    var address  = business.address;
    var contact  = business.contact;
    var hours    = business.hours;

    /* Build areaServed array from seo.local_keywords */
    var areaServed = [];
    if (seo && seo.local_keywords) {
      if (seo.local_keywords.primary) {
        areaServed = areaServed.concat(seo.local_keywords.primary);
      }
      if (seo.local_keywords.secondary) {
        areaServed = areaServed.concat(seo.local_keywords.secondary);
      }
    }

    var schema = {
      '@context': 'https://schema.org',
      '@type': [
        'LocalBusiness',
        'DanceSchool',
        'YogaStudio'
      ],
      '@id': project.domain + '/#business',
      'name': business.legal_name,
      'url': project.domain,
      'description': project.tagline,
      'address': {
        '@type': 'PostalAddress',
        'streetAddress':   address.street,
        'addressLocality': address.suburb,
        'addressRegion':   address.state,
        'postalCode':      address.postcode,
        'addressCountry':  'AU'
      },
      'geo': {
        '@type':     'GeoCoordinates',
        'latitude':  address.geo.latitude,
        'longitude': address.geo.longitude
      },
      'email': contact.email,
      'openingHours': formatOpeningHours(hours),
      'areaServed': areaServed.map(function (area) {
        return {
          '@type': 'City',
          'name': area
        };
      }),
      'priceRange': '$$',
      'currenciesAccepted': 'AUD',
      'paymentAccepted': 'Cash, Credit Card',
      'hasMap': 'https://maps.app.goo.gl/UMrxgrQbENHh1y7U9'
    };

    /* Only add phone if not a placeholder */
    if (contact.phone && contact.phone.indexOf('PLACEHOLDER') === -1) {
      schema['telephone'] = contact.phone;
    }

    /* Only add social links if not placeholders */
    var sameAs = [
      'https://maps.app.goo.gl/UMrxgrQbENHh1y7U9'
    ];
    if (contact.instagram && contact.instagram.indexOf('PLACEHOLDER') === -1) {
      sameAs.push(contact.instagram);
    }
    if (contact.facebook && contact.facebook.indexOf('PLACEHOLDER') === -1) {
      sameAs.push(contact.facebook);
    }
    schema['sameAs'] = sameAs;

    return buildScriptTag(schema);
  });
}


/* ==========================================================================
   2. generateBreadcrumbSchema(breadcrumbs)
   Schema type: BreadcrumbList
   ========================================================================== */

/**
 * Generates a BreadcrumbList JSON-LD schema tag.
 *
 * @param {Array<{name: string, url: string}>} breadcrumbs
 *   Array of breadcrumb items in order, e.g.:
 *   [
 *     { name: 'Home',   url: 'https://www.undrgrnd.com.au/' },
 *     { name: 'Adults', url: 'https://www.undrgrnd.com.au/adults.html' }
 *   ]
 * @returns {string} Complete <script type="application/ld+json"> tag
 */
function generateBreadcrumbSchema(breadcrumbs) {
  if (!Array.isArray(breadcrumbs) || breadcrumbs.length === 0) {
    console.warn('schema-generator: generateBreadcrumbSchema — breadcrumbs must be a non-empty array');
    return '';
  }

  var listItems = breadcrumbs.map(function (item, index) {
    return {
      '@type':    'ListItem',
      'position': index + 1,
      'name':     item.name,
      'item':     item.url
    };
  });

  var schema = {
    '@context':        'https://schema.org',
    '@type':           'BreadcrumbList',
    'itemListElement': listItems
  };

  return buildScriptTag(schema);
}


/* ==========================================================================
   3. generateServiceSchema(program)
   Schema type: Service
   Data source: program object from site-config.json programs.*
   ========================================================================== */

/**
 * Generates a Service JSON-LD schema tag for a single program.
 *
 * @param {Object} program — A program object from site-config.json programs.*
 *   Expected fields: id, name, category, level, short_description,
 *                    estimated_pricing, slug
 * @returns {Promise<string>} Promise resolving to <script> tag string
 */
function generateServiceSchema(program) {
  if (!program || !program.name) {
    console.warn('schema-generator: generateServiceSchema — invalid program object');
    return Promise.resolve('');
  }

  return loadSiteConfig().then(function (config) {
    var business = config.business;
    var project  = config.project;

    /* Build Offer from single price field */
    var offers = [];
    if (program.price) {
      offers.push({
        '@type':         'Offer',
        'name':          'Per Class',
        'price':         program.price,
        'priceCurrency': 'AUD',
        'availability':  'https://schema.org/InStock',
        'url':           project.domain + '/programs/' + (program.slug || program.id) + '.html'
      });
    }

    var schema = {
      '@context':   'https://schema.org',
      '@type':      'Service',
      '@id':        project.domain + '/programs/' + (program.slug || program.id) + '.html#service',
      'name':       program.name,
      'description': program.short_description || program.full_description || '',
      'serviceType': program.category,
      'provider': {
        '@type': 'LocalBusiness',
        'name':  business.legal_name,
        'url':   project.domain
      },
      'areaServed': {
        '@type': 'City',
        'name':  business.address.suburb + ', ' + business.address.state
      },
      'url': project.domain + '/programs/' + (program.slug || program.id) + '.html'
    };

    /* Add audience/level if present */
    if (program.level) {
      schema['audience'] = {
        '@type':       'Audience',
        'audienceType': program.level
      };
    }

    /* Add offers if any pricing was found */
    if (offers.length === 1) {
      schema['offers'] = offers[0];
    } else if (offers.length > 1) {
      schema['offers'] = offers;
    }

    /* Flag medical clearance requirement if applicable */
    if (program.medical_clearance_required) {
      schema['termsOfService'] = 'Medical clearance from a healthcare provider is required before participating in this program.';
    }

    return buildScriptTag(schema);
  });
}


/* ==========================================================================
   4. generateFAQSchema(faqs)
   Schema type: FAQPage
   ========================================================================== */

/**
 * Generates a FAQPage JSON-LD schema tag.
 *
 * @param {Array<{question: string, answer: string}>} faqs
 *   Array of FAQ objects, e.g.:
 *   [
 *     { question: 'Do I need experience?', answer: 'No experience needed...' },
 *     { question: 'What should I wear?',   answer: 'Comfortable clothes...' }
 *   ]
 * @returns {string} Complete <script type="application/ld+json"> tag
 */
function generateFAQSchema(faqs) {
  if (!Array.isArray(faqs) || faqs.length === 0) {
    console.warn('schema-generator: generateFAQSchema — faqs must be a non-empty array');
    return '';
  }

  var entities = faqs.map(function (faq) {
    return {
      '@type':          'Question',
      'name':           faq.question,
      'acceptedAnswer': {
        '@type': 'Answer',
        'text':  faq.answer
      }
    };
  });

  var schema = {
    '@context':   'https://schema.org',
    '@type':      'FAQPage',
    'mainEntity': entities
  };

  return buildScriptTag(schema);
}


/* ==========================================================================
   EXPORT
   Makes functions available as module exports (Node.js / bundlers)
   and also as globals on window for direct browser script tag usage.
   ========================================================================== */

/* Browser global exposure */
if (typeof window !== 'undefined') {
  window.SchemaGenerator = {
    loadSiteConfig:             loadSiteConfig,
    generateLocalBusinessSchema: generateLocalBusinessSchema,
    generateBreadcrumbSchema:   generateBreadcrumbSchema,
    generateServiceSchema:      generateServiceSchema,
    generateFAQSchema:          generateFAQSchema
  };
}

/* CommonJS / Node.js module export */
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    loadSiteConfig:             loadSiteConfig,
    generateLocalBusinessSchema: generateLocalBusinessSchema,
    generateBreadcrumbSchema:   generateBreadcrumbSchema,
    generateServiceSchema:      generateServiceSchema,
    generateFAQSchema:          generateFAQSchema
  };
}
