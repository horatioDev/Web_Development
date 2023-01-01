// To-Do List
// Event Listener
document.addEventListener('DOMContentLoaded', function() {
  // Prevent default behavior / disable submit until a task is typed
  document.querySelector('#submit').disabled = true;
  
  // Event Handler
  document.querySelector('#task').onkeyup = () => {
    // Check if any input in text field
    if (document.querySelector('#task').value.length > 0) {
      // Disable submit
      document.querySelector('#submit').disabled = false;
    } else {
      // Re-enable submit
      document.querySelector('#submit').disabled = true;

    }
  };
   
  document.querySelector('form').onsubmit = () => {
    
    // Create task instance
    const task = document.querySelector('#task').value;
    
    // Create a new list item
    const li = document.createElement('li');
    
    
    // Put task in li html
    li.innerHTML = task;
    
    // Place list item in ul
    document.querySelector('#tasks').append(li);
    
    // Clear input field
    document.querySelector('#task').value = '';
    
    // Log task
    console.log(task);
    
    // Disable button again
    document.querySelector('#submit').disabled = true;

    // Stop submission
    return false;
  }
});