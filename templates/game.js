document.getElementById('resetForm').addEventListener('submit', function(event) {
    // Prevent the form from submitting normally
    event.preventDefault();
  
    // Make an AJAX request to the server
    fetch(this.action, {
      method: this.method
    })
    .then(function(response) {
      if (response.ok) {
        // If the response is ok, reload the page
        location.reload();
      } else {
        // If there was an error, log it to the console
        console.error('Error: ' + response.statusText);
      }
    })
    .catch(function(error) {
      // If there was an error with the fetch request, log it to the console
      console.error('Fetch Error: ' + error.message);
    });
  });