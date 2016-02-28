window.onload = function() {
	// var body = document.querySelector("body");
	// var padding = parseInt(window.getComputedStyle(document.querySelector("nav")).height);
	// body.style.paddingTop = padding + 5 + "px";

	var radioButtons = document.getElementById("judging").querySelectorAll("input");
	for(var i = 0; i < radioButtons.length; i++) {
		radioButtons[i].onclick = updateVotedPlayer;
	}

	document.getElementById("vote").onclick = submitVote;

	var buttons = document.querySelectorAll("li button");
	for(var i = 0; i < buttons.length; i++) {
		buttons[i].onclick = submitCaption;
	}

	document.getElementById("judgebutton").onclick = judge;

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
	// console.log("butthole");
	// var playerName = this.parentNode.querySelector(".listname").innerHTML;
	this.parentNode.parentNode.querySelector(".captioninput").style.display = "none";
	this.parentNode.parentNode.querySelector(".submittedtext").style.display = "";
	this.parentNode.parentNode.style.backgroundColor = "#bbbbbb";
}

function judge() {
	document.getElementById("submissions").style.display = "none";
	document.getElementById("judging").style.display = "";

	var captions = [];
	var textareas = document.querySelectorAll("li textarea");
	for(var i = 0; i < textareas.length; i++) {
		console.log("pushing: " + textareas[i].value);
		captions.push(textareas[i].value);
	}

	console.log(captions);
	var quotes = document.querySelectorAll("#judging q");
	for(var i = 0; i < quotes.length; i++) {
		quotes[i].innerHTML = captions[i];
	}

	captions = null;
}

function submitVote() {
	document.querySelector("form").submit();
}
