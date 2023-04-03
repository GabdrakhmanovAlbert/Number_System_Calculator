function view_change(view_block) {
  const navBar = document.getElementById("select-bar").children;
  const active_block = document.querySelector(".active");
  const pageContainer = document.querySelector(".page-container").children;
  active_block.classList.remove("active");
  navBar[view_block].classList.add("active");
  for (let i = 0; i < pageContainer.length; i++) {
    if (i == view_block) {
      pageContainer[i].style.display = "block";
    } else {
      pageContainer[i].style.display = "none";
    }
  }
}
