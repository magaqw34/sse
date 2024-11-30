// script.js

// Connect to the SSE endpoint
const eventSource = new EventSource('http://127.0.0.1:5000/updateTime');

// When a message is received from the server
eventSource.onmessage = function (event) {

  const eventDisplay = document.getElementById('event-display');
  eventDisplay.textContent = `Current Time: ${event.data}`;

};

// Optional: Handle connection errors
eventSource.onerror = function () {
  console.error('Error connecting to the SSE endpoint.');
};
