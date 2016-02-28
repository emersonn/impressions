window.onload = function() {
	// var body = document.querySelector("body");
	// var padding = parseInt(window.getComputedStyle(document.querySelector("nav")).height);
	// body.style.paddingTop = padding + 5 + "px";

	var radioButtons = document.getElementById("judging").querySelectorAll("input");
	for(var i = 0; i < radioButtons.length; i++) {
		radioButtons[i].onclick = updateVotedPlayer;
	}

	document.getElementById("vote").onclick = submitVote;
	document.querySelector("li button").onclick = submitCaption;
};

function updateVotedPlayer() {
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

function submitCaption() {
	// var playerName = this.parentNode.querySelector(".listname").innerHTML;
	this.parentNode.parentNode.querySelector(".captioninput").style.display = "none";
	this.parentNode.parentNode.querySelector(".submittedtext").style.display = "";
	this.parentNode.parentNode.style.backgroundColor = "#bbbbbb";
}

function submitVote() {
	document.querySelector("form").submit();
}