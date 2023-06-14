const inspirationalButton = document.querySelector('#inspirational-button');
const inspirationalImage = document.querySelector('#inspirational-image');
const inspirationalPhrase = document.createElement('p');
inspirationalButton.addEventListener('click', () => {
  const phrase = prompt('Enter an inspiring phrase:');
  inspirationalPhrase.textContent = phrase;
  inspirationalImage.insertAdjacentElement('beforebegin', inspirationalPhrase);
});