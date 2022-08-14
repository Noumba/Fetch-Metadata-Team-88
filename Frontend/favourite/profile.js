const [link_div_1, link_div_2, link_div_3, link_div_4, link_div_5] =
  document.querySelectorAll(".link_div");

const [icon_1, icon_2, icon_3, icon_4, icon_5] =
  document.querySelectorAll(".icon_image");

const [link_text_1, link_text_2, link_text_3, link_text_4, link_text_5] =
  document.querySelectorAll(".profile-link");

link_text_1.classList.add("selected_link_text");
link_div_1.classList.add("selected_link_div");

const sideMenu = document.getElementById("side_menu");
const burger = document.getElementById("burger");

link_div_1.addEventListener("click", () => {
  link_div_1.classList.add("selected_link_div");
  link_div_2.classList.remove("selected_link_div");
  link_div_3.classList.remove("selected_link_div");
  link_div_4.classList.remove("selected_link_div");
  link_div_5.classList.remove("selected_link_div");
  icon_1.classList.remove("selected_icon");
  icon_2.classList.remove("selected_icon");
  icon_3.classList.remove("selected_icon");
  icon_4.classList.remove("selected_icon");
  icon_5.classList.remove("selected_icon");
  link_text_1.classList.add("selected_link_text");
  link_text_2.classList.remove("selected_link_text");
  link_text_3.classList.remove("selected_link_text");
  link_text_4.classList.remove("selected_link_text");
  link_text_5.classList.remove("selected_link_text");
});

link_div_2.addEventListener("click", () => {
  link_div_2.classList.add("selected_link_div");
  link_div_1.classList.remove("selected_link_div");
  link_div_3.classList.remove("selected_link_div");
  link_div_4.classList.remove("selected_link_div");
  link_div_5.classList.remove("selected_link_div");
  icon_2.classList.add("selected_icon");
  icon_1.classList.add("selected_icon");
  icon_3.classList.remove("selected_icon");
  icon_4.classList.remove("selected_icon");
  icon_5.classList.remove("selected_icon");
  link_text_1.classList.remove("selected_link_text");
  link_text_2.classList.add("selected_link_text");
  link_text_3.classList.remove("selected_link_text");
  link_text_4.classList.remove("selected_link_text");
  link_text_5.classList.remove("selected_link_text");
});

link_div_3.addEventListener("click", () => {
  link_div_3.classList.add("selected_link_div");
  link_div_1.classList.remove("selected_link_div");
  link_div_2.classList.remove("selected_link_div");
  link_div_4.classList.remove("selected_link_div");
  link_div_5.classList.remove("selected_link_div");
  icon_3.classList.add("selected_icon");
  icon_1.classList.add("selected_icon");
  icon_2.classList.remove("selected_icon");
  icon_4.classList.remove("selected_icon");
  icon_5.classList.remove("selected_icon");
  link_text_1.classList.remove("selected_link_text");
  link_text_2.classList.remove("selected_link_text");
  link_text_3.classList.add("selected_link_text");
  link_text_4.classList.remove("selected_link_text");
  link_text_5.classList.remove("selected_link_text");
});

link_div_4.addEventListener("click", () => {
  link_div_4.classList.add("selected_link_div");
  link_div_1.classList.remove("selected_link_div");
  link_div_2.classList.remove("selected_link_div");
  link_div_3.classList.remove("selected_link_div");
  link_div_5.classList.remove("selected_link_div");
  icon_4.classList.add("selected_icon");
  icon_1.classList.add("selected_icon");
  icon_3.classList.remove("selected_icon");
  icon_2.classList.remove("selected_icon");
  icon_5.classList.remove("selected_icon");
  link_text_1.classList.remove("selected_link_text");
  link_text_2.classList.remove("selected_link_text");
  link_text_3.classList.remove("selected_link_text");
  link_text_4.classList.add("selected_link_text");
  link_text_5.classList.remove("selected_link_text");
});

link_div_5.addEventListener("click", () => {
  link_div_5.classList.add("selected_link_div");
  link_div_1.classList.remove("selected_link_div");
  link_div_2.classList.remove("selected_link_div");
  link_div_3.classList.remove("selected_link_div");
  link_div_4.classList.remove("selected_link_div");
  icon_5.classList.add("selected_icon");
  icon_1.classList.add("selected_icon");
  icon_3.classList.remove("selected_icon");
  icon_4.classList.remove("selected_icon");
  icon_2.classList.remove("selected_icon");
  link_text_1.classList.remove("selected_link_text");
  link_text_2.classList.remove("selected_link_text");
  link_text_3.classList.remove("selected_link_text");
  link_text_4.classList.remove("selected_link_text");
  link_text_5.classList.add("selected_link_text");
});

burger.addEventListener("click", () => {
  sideMenu.classList.toggle("side_menu_visible");
});
