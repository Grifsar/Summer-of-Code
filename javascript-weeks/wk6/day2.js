//In JavaScript the prototype is a real object that can be called, instead of an abstract class
//Stopped at 1 hour mark
let f = function () {
	this.a = 1
	this.b = 2
}

let Person = function (name, age) {
	this.name = name
	this.age = age
}
//a function can be added to any object

let paulaB = new  Person("PaulaB", 16)

console.log(paulaB)
Person.prototype.favFood = "green tea cake"
Person.prototype.age = 21
console.log(paulaB.favFood)
console.log(paulaB.age)

var o = {
	a: 2,
	m: function() {
		return this.a +1
	}
}
var p = Object.create(o)
console.log(o.m())
console.log('p.a', p.a)
p.a = 4
console.log(p.m())//takes the p and runs the function on it

//Ways to create objects
//1. syntax

var o = {a: 1}
var students = ["Rox", "Cristina"]//arrays

//2. Constructor
function Graph(){
	this.vertices = []
	this.edges = []
}

Graph.prototype.addVertex = function(v){
	this.vertices.push(v)
}
//3. Object.create

var a = {a: 1}
var b = Object.create(a) //b.a
var c = Object.create(b) //c.a

//4. Class keyword "Sytactic sugar"
'use strict';

class Polygon {
	constructor(height, width) {
		this.height = height
		this.width = width
	}
}

class Square extends Polygon {
	constructor(sideLength) {
		super(sideLength, sideLength)
	}
	get area(){
		this.height * this.width
	}
	set sideLength(newLength) {
		this.height = newLength
		this.width = newLength
	}
}//Longer prototype chains can have performance issues, so you may want to organize them in a way that isn't as intuitive, but is more efficient

new box = new Square(2)

//Homework at roughly 44 minute mark
//Code person and coder "classes"
//Re-implement the underscore.js library's following methods: each, map, reduce using only for loops and maybe foreEach

