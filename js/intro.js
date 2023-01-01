
// Hello function that displays an alert
function hello() {
  alert('Hello, world!')
}

// Variable that won't change
const heading = document.querySelector('h1');

// Manipulate DOM
function hello2() {

  // Toggle by checking the condition 
  // Find the h1 element / change the property
  if (heading.innerHTML === 'Hello') {
    heading.innerHTML = 'Goodbye'
  } else {
    heading.innerHTML = 'Hello'
  }
}


// Form to input name / the get reaction
// Event listener ('event', function)
// Triggered when the structure of the is finished loaded
document.addEventListener('DOMContentLoaded', function() {

  // document.querySelector('form').addEventListener('submit', count);
  document.querySelector('form').onsubmit = function() {
    // Get the id element w/ name and get it's value
    const name = document.querySelector('#name').value;
    // Alert name
    alert(`Hello, ${name}`)
  };
  
})