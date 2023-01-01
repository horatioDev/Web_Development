// API

// API Headers
var myHeaders = new Headers();
myHeaders.append("apikey", "DcuFGEdjlNG30cKQwXrIY6dp96cgVme9");

var requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders
};

// Fetch params
// fetch("https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}", requestOptions)
//   .then(response => response.text())
//   .then(result => console.log(result))
//   .catch(error => console.log('error', error));


// API HttpRequest
document.addEventListener('DOMContentLoaded', function () {

  // Handle form submission
  document.querySelector('form').onsubmit = function() {

    // Make http request to url
    fetch('https://api.apilayer.com/currency_data/live?base=USD', requestOptions)
      // what to w/ promise response
      .then(response =>
        // Convert response to json
        response.json()
      )
      // Save the data to a variable
      .then(data => {
        console.log(data);
        // Get currency input from user
        const currency = document.querySelector('#currency').value.toUpperCase();
  
        // Get quote for currency variable
        const quote = data.quotes[currency];
  
        console.log(quote)
        // CHeck if currency is available
        if (quote !== undefined) {
  
          // Display quote in results div
          document.querySelector('#result').innerHTML = `$1 USD is equal to ${quote.toFixed(3)} ${currency}.`;

        } else {

          // If currency is undefined
          document.querySelector('#result').innerHTML = 'Invalid currency.';
  
        }
      })
      // Catch errors if any
      .catch(error => {
        console.log('Error:', error)
      });
      
      // Prevent form submission
      return false;
  };
  
});