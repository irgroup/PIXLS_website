/**
 * PIXLS Project Website JavaScript
 * Handles navigation, interactive filters, code copy, and BibTeX toggling.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
      mobileToggle.innerHTML = isOpen ? '&#10005;' : '&#9776;';
    });

    // Close menu when clicking a link
    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
        mobileToggle.innerHTML = '&#9776;';
      });
    });
  }

  // 2. Active Navigation Highlight based on scroll position
  const sections = document.querySelectorAll('section[id], header[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => navObserver.observe(section));

  // 3. Copy to Clipboard utility
  window.copySnippet = function(elementId, buttonEl) {
    const target = document.getElementById(elementId);
    if (!target) return;

    const textToCopy = target.innerText || target.textContent;
    navigator.clipboard.writeText(textToCopy.trim()).then(() => {
      const originalText = buttonEl.innerText;
      buttonEl.innerText = 'Copied!';
      buttonEl.classList.add('copied');
      setTimeout(() => {
        buttonEl.innerText = originalText;
        buttonEl.classList.remove('copied');
      }, 2000);
    }).catch(err => {
      console.error('Failed to copy: ', err);
    });
  };

  // 4. Toggle BibTeX visibility
  window.toggleBibtex = function(bibId, buttonEl) {
    const bibBox = document.getElementById(bibId);
    if (!bibBox) return;

    const isShown = bibBox.classList.toggle('show');
    buttonEl.innerText = isShown ? 'Hide BibTeX' : 'BibTeX';
  };

  // 5. Interactive Publication Filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const pubCards = document.querySelectorAll('.pub-card');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      pubCards.forEach(card => {
        if (filterValue === 'all') {
          card.style.display = 'flex';
        } else {
          const categories = (card.getAttribute('data-category') || '').split(' ');
          if (categories.includes(filterValue)) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        }
      });
    });
  });

  // 6. Toggle Blog Post full content
  window.toggleBlog = function(postId, buttonEl) {
    const postBox = document.getElementById(postId);
    if (!postBox) return;

    const isShown = postBox.classList.toggle('show');
    buttonEl.innerText = isShown ? 'Show Less ↑' : 'Read Full Post →';
  };

  // 7. Software Carousel Window Controller
  let currentSoftwareIndex = 0;
  const softwareSlides = document.querySelectorAll('.software-carousel-slide');
  const softwareTabs = document.querySelectorAll('.software-tab-btn');
  const softwareDots = document.querySelectorAll('.carousel-dot');
  const softwareIndicator = document.querySelector('.carousel-indicator-text');

  window.switchSoftwareTab = function(index) {
    const slides = document.querySelectorAll('.software-carousel-slide');
    const tabs = document.querySelectorAll('.software-tab-btn');
    const dots = document.querySelectorAll('.carousel-dot');
    const indicator = document.querySelector('.carousel-indicator-text');
    if (!slides.length) return;

    currentSoftwareIndex = (index + slides.length) % slides.length;

    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === currentSoftwareIndex);
    });

    tabs.forEach((tab, i) => {
      tab.classList.toggle('active', i === currentSoftwareIndex);
    });

    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSoftwareIndex);
    });

    if (indicator) {
      indicator.textContent = `${currentSoftwareIndex + 1} / ${slides.length}`;
    }
  };

  window.nextSoftwareSlide = function() {
    window.switchSoftwareTab(currentSoftwareIndex + 1);
  };

  window.prevSoftwareSlide = function() {
    window.switchSoftwareTab(currentSoftwareIndex - 1);
  };
});

