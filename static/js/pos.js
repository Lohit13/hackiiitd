var button = document.getElementById("but");
var browserWidth = window.innerWidth || document.documentElement.clientWidth;
var browserHeight = window.innerHeight || document.documentElement.clientHeight;
var buttonWidth = button.offsetWidth;
var buttonHeight = button.offsetHeight;

function move() {
    button.style.left = Math.floor(Math.random()*(browserWidth-buttonWidth)) + "px";
    button.style.top = Math.floor(Math.random()*(browserHeight-buttonHeight)) + "px";
}

window.onload = move();