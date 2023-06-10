var tabLinks = document.getElementsByClassName("tablinks");
var tabContents = document.getElementsByClassName("tabcontents");

function openTab(tabname) {
  for (tabLink of tabLinks) {
    tabLink.classList.remove("activelink");
  }
  for (tabContent of tabContents) {
    tabContent.classList.remove("activeTab");
  }
  event.currentTarget.classList.add("activelink");
  document.getElementById(tabname).classList.add("activeTab");
}