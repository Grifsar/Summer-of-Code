// //paramenters are placeholders
// function myFunction(p1, p2) {
// 	return p1 ** p2
// }
// //Arguments are what you pass in
// console.log(myFunction(22, 2))

// //Write function that converts F to C

// function toCelsius(fahrenheit) {
// 	return (fahrenheit - 32) * .5556
// }

// console.log(toCelsius(32))

// document.getElementById("anavirginia").innerHTML = toCelsius(90)
function showName(firstName, lastName) {
	var nameIntro = "Your name is "
	function makeFullName(){//Inner function has access to outer function vars
		return nameIntro + firstName + " " + lastName
	}
	return makeFullName();
}
console.log(showName("Sarah", "Griffiths"))
// $(function() {
// 	var selections = []
// 	$(".myButton").click((){
// 		selections.push(this.prompt("Name"))
// 	})
// })

//Create a button to click above and update #anavirgina to be selections

function celebrityID () {
	var celebrityID = 999
	return{
		getID: function() {
			return celebrityID
		},
		setID: function (theNewID) {
			celebrityID = theNewID
		}
	}
}

var mjID = celebrityID()
console.log(mjID)

console.log(mjID.getID)

mjID.setID(3141)
console.log(mjID.getID())

var x =5

elem = document.getElementById("kasia")
elem.innerHTML = x

// let and const are not hoisted
// initializations are not hoisted either

var y = 7

elem = document.getElementById("kasia")
elem.innerHTML = x + " " + y

function celebrityIDCreator (theCelebrites) {
	var i
	var uniqueID = 100
	for (i = 0; i < theCelebrites.length - 1; i++) {
		theCelebrites[i]["id"] = function () {
			return uniqueID + i
		}
	}
		return theCelebrites
}
var romComCelebs = [{name: "Reese Witherspoon", id:0}, {name: "Julia Roberts", id:0}, {name: "Meg Ryan", id:0}]

var createIdForRomComCelebs = celebrityID (romComCelebs)

var reeseID = createIdForRomComCelebs[0]
console.log(reeseID.id())