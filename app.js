document.addEventListener("DOMContentLoaded", function () {
  // Set the CSRF token value from the cookie
  var csrfToken = getCookie("csrftoken");
  document.getElementById("csrf_token").value = csrfToken;

  document
    .getElementById("customerForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      var formData = new FormData(this);

      fetch("http://127.0.0.1:8000/api/customers/", {
        method: "POST",
        body: formData,
        headers: {
          Accept: "application/json",
          "X-CSRFToken": csrfToken,
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(
              "Network response was not ok " + response.statusText
            );
          }
          return response.json();
        })
        .then((data) => {
          if (data.status === 201) {
            document.getElementById("message").innerHTML =
              "Customer added successfully!";
          } else {
            document.getElementById("message").innerHTML =
              "Error adding customer: " + JSON.stringify(data.data);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          document.getElementById("message").innerHTML =
            "Error adding customer. Please try again.";
        });
    });
});

// Function to get a cookie by name
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
