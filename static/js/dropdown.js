var contacts = document.querySelector('.contacts'),
dropdown = document.querySelector('.dropdown');

contacts.addEventListener('click', function() {
dropdown.classList.toggle('active');
})