// function foo(b) {
// 	var a = 10;
// 	return a + b + 11;
// }
// function bar(x){
// 	var y = 3;
// 	return foo(x*y);
// }

// console.log(bar(17));


// // while (queue.waitForMessage()) {
// // 	queue.processNextMessage();
// // }

// const s = new Date().getSeconds();

// setTimeout(function() {
// 	console.log("Ran after " + (new Date().getSeconds() -s) + " seconds");
// }), 500;

// while(true) {
// 	if (new Date().getSeconds() - s >= 2){
// 		console.log("Good, 2 seconds have passed, we were happily looping");
// 		break;
// 	}
// }

// (function () {
// 	console.log('Kasia W: This is the start.');

// 	setTimeout(function cb(){
// 		console.log('Kat Martin: This is a message from the 0th callback');
// 	});

// 	console.log('This is just a incoming <3');

// 	setTimeout(function cb1(){
// 		console.log('Krstal: Bless you! From call back 1');
// 	});

// 	console.log('Virginia: This is the end.');
// })();

// //const - can't reassign variable to something else - assign it all in one line
// //can't change the pointer
// //let - has block scope
function echo(){
	for (var i = 0; i < arguments.length; i++) {
		console.log(arguments[i]);
	}
}

echo();
echo('bla');
echo('foo', 'bar', 'baz');
//See this for instructions https://github.com/advanced-js/countdown
console.log("Count down");
function countdown(seconds){

	while (seconds > 0) {
		setTimeout()
		console.log(seconds);
		seconds-=1;
	}

}

countdown(5);