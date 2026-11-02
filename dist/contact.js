const contactForm = document.querySelector('[data-contact-form]');

contactForm?.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!contactForm.reportValidity()) return;

  const fields = new FormData(contactForm);
  const name = String(fields.get('name')).trim();
  const email = String(fields.get('email')).trim();
  const message = String(fields.get('message')).trim();
  const subject = `Portfolio inquiry from ${name}`;
  const body = `${message}\r\n\r\nFrom: ${name}\r\nEmail: ${email}`;
  const mailto = `mailto:arblankenbiller@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

  window.location.href = mailto;
  document.querySelector('[data-form-status]').textContent =
    'Your email app will open with your draft. Send it there to complete your message. If it does not open, email arblankenbiller@gmail.com directly.';
});
