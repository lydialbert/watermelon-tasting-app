// Event Listener for 'Book' Buttons //

'use strict';

const bookButton = document.querySelector('.book-it');

bookButton.addEventListener('click', (evt) => {
    evt.preventDefault();

    alert('Successfully Booked!')
});