var numPlayers = 0;

window.onload = function() {
	var body = document.querySelector("body");
	var padding = parseInt(window.getComputedStyle(document.querySelector("nav")).height);
	body.style.paddingTop = padding + 5 + "px";
	document.getElementById("addplayer").onclick = addNewPlayer;
	document.getElementById("start").onclick = submitForm;
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
	removeButton.innerHTML = "-";
	removeButton.onclick = removePlayer;
	//removeButton.className = "remove";
	removeButton.classList.add("btn");
	removeButton.classList.add("btn-lg");
	removeButton.classList.add("btn-primary");
	removeButton.type = "button";

	playerNameDiv.className = "playername";
	playerNameDiv.innerHTML = playerName;

	/*incScoreButton.className = "changescore";
	decScoreButton.className = "changescore";
	incScoreButton.id = "incscoreplayer" + numPlayers;
	decScoreButton.id = "decscoreplayer" + numPlayers;
	incScoreButton.innerHTML = "+";
	decScoreButton.innerHTML = "-";*/

	// playerNameDiv.style.marginTop = parseInt(window.getComputedStyle(document.getElementById("addplayerli")).height) / 2 + "px";
	newPlayerDiv.appendChild(removeButton);
	newPlayerDiv.appendChild(playerNameDiv);
	// newPlayerDiv.appendChild(incScoreButton);
	// newPlayerDiv.appendChild(decScoreButton);
	newPlayerLi.id = "li-player-" + playerName;
	newPlayerLi.appendChild(newPlayerDiv);

	var playerList = document.getElementById("playerlist");
	playerlist.insertBefore(newPlayerLi, document.getElementById("addplayerli"));

	document.getElementById("addplayername").value = "";

	var nameInput = document.createElement("input");
	nameInput.id = "input-player-" + playerName;
	nameInput.type = "hidden";
	nameInput.name = "names[player-" + playerName + "]";
	nameInput.value = playerName;
	document.querySelector("form").appendChild(nameInput);
	numPlayers++;
}

function removePlayer() {
	var toRemoveLi = this.parentNode.parentNode;
	var base = "li-player-";
	var playerName = toRemoveLi.id.substring(base.length);
	toRemoveLi.parentNode.removeChild(toRemoveLi);
	var inputToRemove = document.getElementById("input-player-" + playerName);
	inputToRemove.parentNode.removeChild(inputToRemove);
	numPlayers--;
}

function submitForm() {
	document.querySelector("form").submit();
}
