// DOM Manipulation
const increaseBtn = document.getElementById('increase');
const decreaseBtn = document.getElementById('decrease');
const h1 = document.querySelector('h1');

let counter = 0;

// Run this function after page is loaded
document.addEventListener('DOMContentLoaded', () => {
  increaseCount();
  
  decreaseCount();
});


// Functionality
// Increase count
function increaseCount() {
  increaseBtn.addEventListener('click', function(){
    counter++;
    h1.innerHTML = counter;
  })
}

//  Decrease count
function decreaseCount() {
  decreaseBtn.addEventListener('click', function(){
    counter--;
    h1.innerHTML = counter;
  })
}
