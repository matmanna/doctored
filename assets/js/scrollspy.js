/**
 * TOC ScrollSpy
 * Highlights the current section in the table of contents as the user scrolls
 */
function initTocScrollSpy() {
  const headings = document.querySelectorAll('h2[id], h3[id], h4[id], h5[id], h6[id]');
  const tocLinks = document.querySelectorAll('.toc-link');
  
  if (headings.length === 0 || tocLinks.length === 0) return;
  
  // Create a map of heading IDs to TOC links
  const idToTocLink = {};
  tocLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.startsWith('#')) {
      idToTocLink[href.substring(1)] = link;
    }
  });
  
  // Create an array of heading positions for quick lookup
  const headingPositions = Array.from(headings).map(heading => {
    return {
      id: heading.id,
      top: heading.getBoundingClientRect().top + window.pageYOffset - 100
    };
  });
  
  function updateToc() {
    const scrollPosition = window.pageYOffset;
    
    // Find the last heading that's above the current scroll position
    let currentHeadingIndex = headingPositions.findIndex(heading => 
      heading.top > scrollPosition
    ) - 1;
    
    // If we're before the first heading or after finding a match
    if (currentHeadingIndex === -2) {
      currentHeadingIndex = headingPositions.length - 1;
    } else if (currentHeadingIndex < 0) {
      currentHeadingIndex = 0;
    }
    
    // Remove active class from all links
    tocLinks.forEach(link => link.classList.remove('font-bold', 'text-primary-800', 'dark:text-primary-300'));
    
    // Add active class to current link
    const currentId = headingPositions[currentHeadingIndex]?.id;
    if (currentId && idToTocLink[currentId]) {
      idToTocLink[currentId].classList.add('font-bold', 'text-primary-800', 'dark:text-primary-300');
    }
  }
  
  // Initial update
  updateToc();
  
  // Update on scroll with throttling
  let ticking = false;
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        updateToc();
        ticking = false;
      });
      ticking = true;
    }
  });
}

document.addEventListener('DOMContentLoaded', initTocScrollSpy);

