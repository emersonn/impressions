var numPlayers = 0;

window.onload = function() {
	var body = document.querySelector("body");
	var padding = parseInt(window.getComputedStyle(document.querySelector("nav")).height);
	body.style.paddingTop = padding + 5 + "px";
	document.getElementById("addplayer").onclick = addNewPlayer;
};

function addNewPlayer() {
	var playerName = document.getElementById("addplayername").value;
	if(playerName == "") {
		return;
	}
	var newPlayerLi = document.createElement("li");
	newPlayerLi.id = "player" + numPlayers;
	var newPlayerDiv = document.createElement("div");
	newPlayerDiv.className = "player";
	var removeButton = document.createElement("button");
	var playerNameDiv = document.createElement("div");
	// var incScoreButton = document.createElement("button");
	// var decScoreButton = document.createElement("button");
	removeButton.id = "removeplayer" + numPlayers;
	removeButton.innerHTML = "x";
	removeButton.onclick = removePlayer;
	removeButton.className = "remove";

	playerNameDiv.className = "playername";
	playerNameDiv.innerHTML = playerName;

	/*incScoreButton.className = "changescore";
	decScoreButton.className = "changescore";
	incScoreButton.id = "incscoreplayer" + numPlayers;
	decScoreButton.id = "decscoreplayer" + numPlayers;
	incScoreButton.innerHTML = "+";
	decScoreButton.innerHTML = "-";*/

	newPlayerDiv.appendChild(removeButton);
	newPlayerDiv.appendChild(playerNameDiv);
	// newPlayerDiv.appendChild(incScoreButton);
	// newPlayerDiv.appendChild(decScoreButton);

	newPlayerLi.appendChild(newPlayerDiv);

	var playerList = document.getElementById("playerlist");
	playerlist.insertBefore(newPlayerLi, document.getElementById("addplayerli"));

	document.getElementById("addplayername").value = "";
	numPlayers++;
}

function removePlayer() {
	var toRemove = "player" + this.id[this.id.length - 1];
	var toRemoveLi = document.getElementById(toRemove);
	toRemoveLi.parentNode.removeChild(toRemoveLi);

	numPlayers--;
}