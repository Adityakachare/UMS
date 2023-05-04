// Get the roll number text field element
var rollNumberField = document.getElementById("rno");

// Get the last recorded roll number from local storage or set it to 0 if it doesn't exist
var lastRecordedRollNumber = localStorage.getItem("rno") || 0;

// Increment the last recorded roll number by 1
var newRollNumber = parseInt(lastRecordedRollNumber) + 1;

// Update the roll number text field with the new value
rollNumberField.value = newRollNumber;

// Save the updated roll number value to local storage for next time
localStorage.setItem("rno", newRollNumber);
