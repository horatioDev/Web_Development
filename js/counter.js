// Check if counter is already in local  storage if not set value
// Local Storage
// LocalStorage.getItem(key): Get key if exists
// LocalStorage.setItem(key, value): Sets key, value if doesn't exist
if (!localStorage.getItem('counter')) {
  localStorage.setItem('counter', 0)
}

// Count function that increments on click(s)
function count() {
  // Create a variable that set the initial count
  let counter = localStorage.getItem('counter')

  // Increment count by
  // counter = counter + 1
  // counter +=1
  counter++

  // Alert count
  // alert(counter)

  // Manipulate the DOM
  document.querySelector('h1').innerHTML = counter;

  // 
  localStorage.setItem('counter', counter)

  // Check if value is a multiple of ten then alert w/ template literal
  // if (counter % 10 === 0) {
  //   alert(`The count is ${counter}`)
  // }
}

// Event listener ('event', function)
// Triggered when the structure of the is finished loaded
document.addEventListener('DOMContentLoaded', function() {

  // Get current count from local storage / keep current count after reload/refresh/exit
  document.querySelector('h1').innerHTML = localStorage.getItem('counter')
  // document.querySelector('button').addEventListener('click', count);
  document.querySelector('button').onclick = count;
  
  // Set a 1 sec interval
  // setInterval(count, 1000)
})

