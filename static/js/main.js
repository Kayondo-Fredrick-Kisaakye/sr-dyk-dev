const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-links a[href*="#"]');
const sections = document.querySelectorAll('section[id]');
const contactForm = document.querySelector('#contact-form');
const formNote = document.querySelector('#form-note');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}

links.forEach((link) => {
  link.addEventListener('click', (event) => {
    const href = link.getAttribute('href');
    if (!href.includes('#')) return;

    const id = href.split('#')[1];
    const target = document.getElementById(id);
    if (!target) return;

    event.preventDefault();
    target.scrollIntoView({ behavior: 'smooth' });
    navLinks?.classList.remove('open');
  });
});

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach((section) => {
    if (window.scrollY >= section.offsetTop - 120) {
      current = section.id;
    }
  });

  links.forEach((link) => {
    const sectionId = link.getAttribute('href').split('#')[1];
    link.classList.toggle('active', sectionId === current);
  });
});

if (contactForm && formNote) {
  contactForm.addEventListener('submit', () => {
    formNote.textContent = 'Submitting your message...';
  });
}
