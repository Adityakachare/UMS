function validatePassword() {
  var password = document.getElementById("pwd").value;
  var confirmPassword = document.getElementById("cpwd").value;
  if (password != confirmPassword) {
      alert("Passwords do not match.");
      return false;
  }
  return true;
}