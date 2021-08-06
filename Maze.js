// global variables for the game--------------------------------------

var currentPos = [0,0];
var previousPos = [];
var exits = [];
var directions = ["north", "east", "south", "west"];
var layout = [];
var nextStep;
var trapped = false;

// room descriptions---------------------------------------------------

var maze = 
[
[[0,1,0,0],[0,1,1,1],[0,1,1,1],[0,1,0,1],[0,0,1,1]],
[[0,0,1,0],[1,0,1,0],[1,1,0,0],[0,1,1,1],[1,0,1,1]],
[[1,1,1,0],[1,0,1,1],[0,1,0,0],[1,0,1,1],[1,0,0,0]],
[[1,1,1,0],[1,1,0,1],[0,1,0,1],[1,0,1,1],[0,0,1,0]],
[[1,1,0,0],[0,1,0,1],[0,0,0,1],[1,1,0,0],[1,1,0,1]],
];

var description = [
 [["You wake up in an empty room with white walls. No one around but you can hear some noise to the east from you. There's a door ..."],["You enter this room and realize that it looks identical to the previous one but there's a guy sleeping on the floor. You wake him up and he tells you that you both are trapped. These rooms are a labyrinth that he has been trying to escape for the past 10 days but all for nothing. \n \nEspecially because each time you walk from one room to another, the door you have just passed through closes behind you.  \n \nTogether you decide to try again.. "],["Oops..wrong choice. The room is full of spiders. Where do you go next?"],["In this room there's no light"],["You enter the room and an old man greets you. When he makes his first step towards you 20 pistols start firing at the same time and in different directions. The guy backs up and the guns stop. Thankfully, no one's got hurt. He suggests leaving this room as soon as possible"]],
 [["Zombies..zombies..many zombies..oh, no!!! An old man gets bitten and you decide to shoot him rather then let him convert into one of them"],["Half of the room is filled up with guns. But why? Who brought them here? After a short conversation with the guy, both of you agree to take one gun with you in case"],["Another empty room. Let's keep on"],["You enter this room and as soon as your partner closes the room 2 big valves open up automatically letting water out. It starts filling up the room pretty quickly. You don't want to drown..do you? "],["Having entered this room you realize how tired you are. Let's suggest the guy to have some rest"]],
 [["Sirens blare loudly. You probably feel like you head is about to burst and quickly decide to go further..."],["You see a piece of paper on the floor saying 'Good job!' You think to yourself: Who left it here? Does anyone know we're inside this? Can it be a hint that we're going the right way?"],["Empty room..yikes! There's a bunch of skeletons hanging from the ceiling. It couldn't have been creepier than this"],["You enter this room hearing someone telling you 'Do you want to eat?' You ask the guy if he has heard anything, but no..it's only you hearing this voice"],["There is a table with food in the center of the table! They definitely know we're in these rooms. Someone is watching us."]],
 [["The room is so foggy you can't see your palms. You eyes get watery and start hurting. You can't stay in here unless you want to go blind"],["Empty room. Nothing special. However, you decide to look at your watch to see how much time you've been walking around and see that the clock hand is going in a counter-clockwise direction. What is that supposed to mean?"],["There's a three-eyed raven flying around the room.. when it notices you, he rushes to attack.. you panic while see it approaching but you partner manages to shoot the bird. Good thing he has a gun"],["The overall situation starts feeling desperate. You've been walking around and around. But what else is there to do?"],["It's freezing in this room. What's the temperature like..-10.. and your partner allergic to cold temperatures.. better get out"]],
 [["You're partner gets anxious and tells you he can't continue anymore. He wants to split, but you manage to convince him to stay together as you've been helping each other so much thourhgout this journey"],["Money. So much. You can bathe in it. But what's the point of filling your pockets with it if it seems like you'll never escape this curse"],["at this point you are so tired of everything, no patience is left and you start praying hoping there's any way to change the situation"],["You partner says he can't continue like this no more. He begs you to shoot him, but there's no way you can do that. He ends up shooting himself..."],["You see a group of people dressed in black. They announce that you've been selected for this labyrinth as an experimental object for a new government research program that focuses on lonely people just like you. They try to prove that flight-or-fight response of lonely people degrades with the time because they stop caring about life and just go with the flow. \nYou think about it for a moment and realize that this doesn't have any relation to you. You want to live. You must get out. They announce that this room is the last in the labyrinth and now it's only one small decision that separates you from escape. Think carefully. Otherwise you'll be stuck in here forever.."]],
]; 

// retrival of room description-----------------------------------------

function getX(position)
{
  return position[0];
}

function getY(position)
{
  return position[1];
}

function findRoom (position) 
{
	layout = description[getX(position)][getY(position)];
}

function findExits (position) 
{
	exits = maze[getX(position)][getY(position)];
	function removeElementsWithValue(arr, val) 
	{
		var i = arr.length;
		while (i--) 
		{
			if (arr[i] === val) {arr.splice(i, 1);}
		}
		return arr;
	}
	
	if (exits[0] == 1) {exits[0] = directions[0]};
	if (exits[1] == 1) {exits[1] = directions[1]};
	if (exits[2] == 1) {exits[2] = directions[2]};
	if (exits[3] == 1) {exits[3] = directions[3]};
	
	removeElementsWithValue(exits, 0);
}

//traversing functions--------------------------------------------

function goEast (position)
{
	position[1] = position[1]+1;
}

function goWest (position)
{
	position[1] = position[1]-1;
}

function goSouth (position)
{
	position[0] = position[0]+1;
}

function goNorth (position)
{
	position[0] = position[0]-1;
}

//magic door functions-----------------------------------------

function hasExited (position)
{
	position[0] = currentPos[0];
	position[1] = currentPos[1];
}

function isTrapped(position)
{
	if (maze[getX(position)][getY(position)][0] == 0 && maze[getX(position)][getY(position)][1] == 0 && maze[getX(position)][getY(position)][2] == 0 && maze[getX(position)][getY(position)][3] == 0)
	{
		trapped = true;
		alert("You entered the room but there are no more open exits. \n \nYou are trapped! End of the game! :(");
	}
}

function closeEast(prevPos, curPos)
{
	maze[getX(prevPos)][getY(prevPos)][1]	= 0;
	maze[getX(curPos)][getY(curPos)][3]	= 0;
}

function closeWest(prevPos, curPos)
{
	maze[getX(prevPos)][getY(prevPos)][3]	= 0;
	maze[getX(curPos)][getY(curPos)][1]	= 0;
}

function closeNorth(prevPos, curPos)
{
	maze[getX(prevPos)][getY(prevPos)][0]	= 0;
	maze[getX(curPos)][getY(curPos)][2]	= 0;
}

function closeSouth(prevPos, curPos)
{
	maze[getX(prevPos)][getY(prevPos)][2]	= 0;
	maze[getX(curPos)][getY(curPos)][0]	= 0;
}


// successful finishing alert-----------------------------------

function winner()
{
	if (currentPos[1] == maze[1].length) {alert("You made it! Congratulations!")};
}

// main loop of the game----------------------------------------

while (currentPos[1] < maze[1].length  && trapped != true)
{
	findExits(currentPos);
	findRoom(currentPos);
	hasExited(previousPos);
	nextStep = prompt(layout + "\n \nYou see the following exit(s): " + exits + ". \nNow where do you go from here?");
	if (nextStep.toLowerCase() == exits[0] || nextStep.toLowerCase() == exits[1] || nextStep.toLowerCase() == exits[2] || nextStep.toLowerCase() == exits[3])
	{
		
		if (nextStep.toLowerCase() ==  "east") 
			{
				goEast(currentPos);
				winner();
				closeEast(previousPos, currentPos);
			}
			if (nextStep.toLowerCase() ==  "west") 
			{
				goWest(currentPos);
				winner();
				closeWest(previousPos, currentPos);
			}
			if (nextStep.toLowerCase() ==  "north") 
			{
				goNorth(currentPos);
				winner();
				closeNorth(previousPos, currentPos);
			}
			if (nextStep.toLowerCase() ==  "south") 
			{
				goSouth(currentPos);
				winner();
				closeSouth(previousPos, currentPos);
			}
	}
	// in case when user enters a wrong answer
	else {nextStep = prompt("Wrong answer :( Please choose only one of the available exits! \n \nYou see the following exit(s): " + exits + ". \nNow where do you go from here?");
		if (nextStep.toLowerCase() == exits[0] || nextStep.toLowerCase() == exits[1] || nextStep.toLowerCase() == exits[2] || nextStep.toLowerCase() == exits[3]){
			if (nextStep.toLowerCase() ==  "east") 
			{
				goEast(currentPos);
				winner();
				closeEast(previousPos, currentPos);
			}
			if (nextStep.toLowerCase() ==  "west") 
			{
				goWest(currentPos);
				winner();
				closeWest(previousPos, currentPos);
			}
			if (nextStep.toLowerCase() ==  "north") 
			{
				goNorth(currentPos);
				winner();
				closeNorth(previousPos, currentPos);
			}
			if (nextStep.toLowerCase() ==  "south") 
			{
				goSouth(currentPos);
				winner();
				closeSouth(previousPos, currentPos);
			}
			if (currentPos[1] == maze[1].length) {alert("You made it! Congratulations!")};
		}
	}
	isTrapped(currentPos);
}

