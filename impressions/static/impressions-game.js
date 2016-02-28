window.onload = function() {
	var body = document.querySelector("body");
	var padding = parseInt(window.getComputedStyle(document.querySelector("nav")).height);
	body.style.paddingTop = padding + 5 + "px";
};

