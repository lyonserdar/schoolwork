// Constants
const LOGIN_URL =
  "http://universe.tc.uvu.edu/cs2550/assignments/PasswordCheck/check.php";

// Elements
var usernameEl = document.getElementById("username");
var passwordEl = document.getElementById("password");
var authErrorEl = document.getElementById("auth-error");

function login() {
  let username = usernameEl.value;
  let password = passwordEl.value;
  let body = `userName=${username}&password=${password}`;
  let xhr = new XMLHttpRequest();
  xhr.open("POST", LOGIN_URL);
  xhr.responseType = "json";
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function () {
    if (this.status == 200) {
      if (this.response?.result == "invalid") {
        authErrorEl.textContent = "Invalid Credentials.";
      } else {
        localStorage.setItem("cs2550timestamp", JSON.stringify(this.response));
        window.location.replace("game.html");
      }
    } else {
      authErrorEl.textContent = "Server Error.";
    }
  };
  xhr.send(body);
}
