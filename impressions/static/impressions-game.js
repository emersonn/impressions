window.onload = function() {
	var body = document.querySelector("body");
	var padding = parseInt(window.getComputedStyle(document.querySelector("nav")).height);
	body.style.paddingTop = padding + 5 + "px";

	var radioButtons = document.getElementById("judging").querySelectorAll("input");
	for(var i = 0; i < radioButtons.length; i++) {
		radioButtons[i].onclick = updateVotedPlayer;
	}
};

function updateVotedPlayer() {
	console.log("updating selected player:");
	var radioButtons = document.getElementById("judging").querySelectorAll("input");
	for(var i = 0; i < radioButtons.length; i++) {
		var parentDiv = radioButtons[i].parentNode;
		parentDiv.classList.remove("votedplayer");
	}
	var parentDiv = this.parentNode;
	if(! parentDiv.classList.contains("votedplayer")) {
		parentDiv.classList.add("votedplayer");
	}
}
