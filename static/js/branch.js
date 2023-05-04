var fieldSelect = document.getElementById("field");
var branchSelect = document.getElementById("branch");

fieldSelect.addEventListener("change", function() {
  var field = this.value;
  if (field === "B.Tech") {
    updateBranchOptions(["Computer Engineering", "Information Technology Engineering", "Electronics and Telecommunication Engineering", "Electrical Engineering"]);
  } else if (field === "M.Tech") {
    updateBranchOptions(["Computer Engineering", "Information Technology Engineering", "Electronics Engineering", "Civil Engineering"]);
  } else if (field === "BSc") {
    updateBranchOptions(["Information Technology", "Physics", "Chemistry", "Maths"]);
  } else if (field === "MSc") {
    updateBranchOptions(["Information Technology", "Artificial Intelligence", "Computer Science", "Data Science"]);
  } else {
    updateBranchOptions([]);
  }
});

function updateBranchOptions(options) {
  branchSelect.innerHTML = "";
  for (var i = 0; i < options.length; i++) {
    var option = document.createElement("option");
    option.text = options[i];
    option.value = options[i];
    branchSelect.add(option);
  }
}