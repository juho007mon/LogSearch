function performSearch() {
  var query = document.getElementById('search-box').value;
  // You can use a fetch request to the Flask backend to perform the search
  fetch('/search?query=' + encodeURIComponent(query))
      .then(response => response.json())
      .then(data => {
          // Process and display the search results
          console.log(data);
      })
      .catch(error => console.error('Error:', error));
}