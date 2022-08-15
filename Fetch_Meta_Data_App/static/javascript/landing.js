const Burger = document.getElementById("burger");
const Menu = document.getElementById("menu");
const header = document.getElementById("hero");
const trust = document.getElementById("trust");
const Line_1 = document.getElementById("line_1");
const Line_2 = document.getElementById("line_2");
const Line_3 = document.getElementById("line_3");
const [
  arrow_1,
  arrow_2,
  arrow_3,
  arrow_4,
  arrow_5,
  arrow_6,
] = document.querySelectorAll(".arrow-down");
const [
  question_1,
  question_2,
  question_3,
  question_4,
  question_5,
  question_6
] = document.querySelectorAll(".question");
const [
  questions_hide_1,
  questions_hide_2,
  questions_hide_3,
  questions_hide_4,
  questions_hide_5,
  questions_hide_6,
] = document.querySelectorAll(".question_hide");

const [para_1, para_2, para_3, para_4, para_5, para_6] =
  document.querySelectorAll(".question_paragragh");

const arrow_div_1 = document.getElementById("arrow_div_1");

Burger.addEventListener("click", () => {
  Burger.classList.toggle("active-burger");
  Menu.classList.toggle("button_div_active");
  Line_1.classList.toggle("line_1");
  Line_2.classList.toggle("line_2");
  Line_3.classList.toggle("line_3");
});

header.addEventListener("click", () => {
  Menu.classList.remove("button_div_active");
  Burger.classList.remove("active-burger");
  Line_1.classList.remove("line_1");
  Line_2.classList.remove("line_2");
  Line_3.classList.remove("line_3");
  console.log("hi");
});

trust.addEventListener("click", () => {
  Menu.classList.remove("button_div_active");
  console.log("hi");
});

questions_hide_1.addEventListener("click", () => {
  arrow_1.classList.toggle("arrow-up");
  question_1.classList.toggle("active-question");
  para_1.classList.toggle("question_paragragh_show");
});

questions_hide_2.addEventListener("click", () => {
  arrow_2.classList.toggle("arrow-up");
  question_2.classList.toggle("active-question");
  para_2.classList.toggle("question_paragragh_show");
});

questions_hide_3.addEventListener("click", () => {
  arrow_3.classList.toggle("arrow-up");
  question_3.classList.toggle("active-question_2");
  para_3.classList.toggle("question_paragragh_show");
});

questions_hide_4.addEventListener("click", () => {
  arrow_4.classList.toggle("arrow-up");
  question_4.classList.toggle("active-question");
  para_4.classList.toggle("question_paragragh_show");
});

questions_hide_5.addEventListener("click", () => {
  arrow_5.classList.toggle("arrow-up");
  question_5.classList.toggle("active-question");
  para_5.classList.toggle("question_paragragh_show");
});

questions_hide_6.addEventListener("click", () => {
  arrow_6.classList.toggle("arrow-up");
  question_6.classList.toggle("active-question_2");
  para_6.classList.toggle("question_paragragh_show");
});
