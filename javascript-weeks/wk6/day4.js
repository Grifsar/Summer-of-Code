//Stopped at 48:34
// //Promise = reps eventual completion or failure of an action
// var promise1 = new Promise(function(resolve, reject){
// 	// success value, failure reason
// 	setTimeout(resolve, 100, 'Good morning ladies!');
// });

// console.log(promise1);

// var promise2 = new Promise((resolve, reject) =>{
// 	setTimeout(function(){
// 		resolve("Success!")
// 	}, 250)
// });
// promise2.then((successMessage) => {
// 	console.log("Yay! " + successMessage);
// })
// //Promise can be in one of 3 states
// //pending, fulfilled, rejected
// //fullfilled and rejected are settled states
// //.then handles fulfilled state
// //.catch handles rejected state
// //.then function lives on Promise.prototype
// //Promise.prototype.finally(onFinally) runs when the Promise is settled
// //same goes for .catch for failure state
// //promises can be chained
// //Promise.length always returns 1
// //Methods
// //Promise.all(iterable) - goes after everything has been fulfilled or rejected
// //Promise.race(iterable) - goes as soon as a single promise fulfills or rejects
// //Promise.reject(reason) - returns a promise that is rejected with the reason
// //Promise.resolve(value) - returns with the reason it succeeded
// //.resolve if you don't know if it is a Promoise or not
// //Arguments to 'then' are optional, and 'catch(failueCallback') is shorthand for 'then(null, failureCallback)'
// // Short cuts
// // Promise.resolve() and Promise.reject() manually create an already resolved / rejected promise.


// function myAsyncFunction(url) {
// 	return new Promise((resolve, reject) => {
// 		const xhr = new XMLHttpRequest();
// 		xhr.open('GET', url);
// 		xhr.onload = () => resolve(xhr.responseText);
// 		xhr.onerror = () => reject(xhr.statusText);
// 		xhr.send();
// 	});
// }

'use strict;'

var promiseCount = 0;
function testPromise(){
	let thisPromiseCount = ++promiseCount;
	let log = document.getElementById('log');
	log.insertAdjacentHTML('beforeend', thisPromiseCount + ') Started(<small>Sync code started</small><br/>');

	let p1 = new Promise((resolve, reject) => {
		log.insertAdjacentHTML('beforeend', thisPromiseCount + ') Promise started (<small>Async code started</small>)<br/>');
		window.setTimeout(function(){
			resolve(thisPromiseCount);
		}, Math.random() * 2000 + 1000);
	});

	p1.then(
		function(val){
			log.insertAdjacentHTML('beforeend', val + ')<small>Async code terminated</small>)<br/>');
		}).catch((reason) => {
			console.log('Handle rejeced promise ('+reason+') here.');
		});
		log.insertAdjacentHTML('beforeend', thisPromiseCount + ') Promise made (<small>Sync code terminated</small><br/>');
} if ("Promise" in window) {
	let btn = document.getElementById("btn");
	btn.addEventListener("click", testPromise);	
} else {
	log = document.getElementById('log');
	log.innerHTML = "Cannot run the live example because your browser doesn't support Promise intereface"
}

const promise3 = promise2().then(successCallback, failureCallback)