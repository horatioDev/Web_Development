// Event listener ('event', function)
// Triggered when the structure of the is finished loaded
document.addEventListener('DOMContentLoaded', function () {

  // // Change font to red
  // document.querySelector('#red').onclick = function () {
  //   document.querySelector('#hello').style.color = 'red';

  // };

  // // Change font to blue
  // document.querySelector('#blue').onclick = function () {
  //   document.querySelector('#hello').style.color = 'blue';

  // };

  // // Change font to green
  // document.querySelector('#green').onclick = function () {
  //   document.querySelector('#hello').style.color = 'green';

  // };

  // Get all of the data color attrs w/ forEach
  // Loop and add an event handler
  document.querySelectorAll('button').forEach(function(button){
    button.onclick = function() {
      document.querySelector('#hello').style.color = button.dataset.color;
    };
  });

  // Get select from dropdown option
  document.querySelector('select').onchange = function() {
    document.querySelector('#hello').style.color = this.value;
  }
})