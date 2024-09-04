"use strict";

const stacklinesbutton = document.querySelector(".stacklines");
const loginbox = document.querySelector(".boxlogin");
// const overlay = document.querySelector(".overlay");

const openorclose = function () {
  loginbox.classList.toggle("hidden");
  overlay.classList.toggle("hidden");
};

const closebox = function () {
  loginbox.classList.add("hidden");
  overlay.classList.add("hidden");
};

stacklinesbutton.addEventListener("click", openorclose);

// overlay.addEventListener("click", closebox);
// body1.addEventListener("click", closebox);
