const inputs = document.querySelectorAll(".input");

function focusF() {
  let prnt = this.parentNode;
  prnt.classList.add("focus");
}

function remF() {
  let prnt = this.parentNode;
  if (this.value == "") {
    prnt.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusF);
  input.addEventListener("blur", remF);
});
