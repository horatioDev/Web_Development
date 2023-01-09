// Create a show page function that shows the page passed as an argument
function show_page(page) {
  // Hide each page(s) w/ for each loop
  document.querySelectorAll('div').forEach(div => {
    // Set display to none
    div.style.display = 'none';
  })
  
  // Show the page that is passed as argument
  document.querySelector(`#${page}`).style.display = 'block';

}

// Listen for page to be loaded
document.addEventListener('DOMContentLoaded', function() {
  // Loop through buttons and add event listener
  
  // #1
  // document.querySelectorAll('button').forEach(button => {
  //   button.addEventListener('click', function() {
  //     // Use this keyword to reference the button clicked
  //     show_page(this.dataset.page);
  //   })
  // })
  
  // #2
  document.querySelectorAll('button').forEach(button => {
    button.onclick = function() {
      // Use this keyword to reference the button clicked
      show_page(this.dataset.page);
    }
  })
  
  
})