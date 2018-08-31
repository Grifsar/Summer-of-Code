#Stopped at 45:31
#Dictionaries - can't change the order. Can't change the key - you can only copy the value into a new key and delete the old one

#Instantiating
# dict(name = "", discord_id= "", fav_food = "")#This is a contructor
# anne_niekrenz = dict(name = "Anne", discord_id = "anne", fav_food = "ice cream")
# print(anne_niekrenz)

# #Notation
my_dict = {
	"a": 35000,
	"b": 8000,
	"z":450
}
my_dict["d"] = my_dict["a"]
del(my_dict["a"])
print(my_dict["d"])
# print(my_dict)

# # access items
# print(my_dict["a"])

# # add
# my_dict["c"] = 3000
# print(my_dict["c"])
# print(my_dict)
# # modify
# #my_dict["a"] = 50

# # delete item
# del(my_dict["a"])
# print(my_dict)
# delete dictionary
# del(my_dict) will delete it and you'll get an error if you try to print it

sarah_dict = {
	"name": "Sarah",
	"birthday": "October 11th",
	"pet": "Selene the cat",
	"fav_food": "Pizza",
	"graduated_from": "Westminster College"
}
print("My name is " + sarah_dict["name"] + ". My birthday is " + sarah_dict["birthday"] + ". My pet is " + sarah_dict["pet"] + 
	". My favorite food is " + sarah_dict["fav_food"] + ". I graduated from "	+ sarah_dict["graduated_from"] + "." )
#Classes

# class Student():
# 	discord_id = "Virginia [Gold] [Volunteer]"

# s1 = Student()
# print(s1.discord_id)


class Student():
	def __init__(self, name, ask_id, fav_food, dream):
		self.name = name
		self.discord_id = ask_id
		self.fav_food = fav_food
		self.dream = dream

	def my_print(self):
		print(self.name + " " + self.discord_id + " " + self.fav_food + " " + self.dream)

s1 = Student("Virginia Balseiro","Virginia [Gold] [Volunteer]", "pasta", "moving to europe and working as a dev in a vegan company!!")
s2 = Student("Andreea Visanoiu"," ", "wontonmee", "becoming an University teacher")
s3 = Student("Deb Cupitt"," ", "Chocolate!", "gender equity")
s4 = Student("Marwa Qabeel","​Marwa Qabeel [Gold]", "", "Data Analyst")
s5 = Student("Sacha Young","​sacha[Gold]", "french fries", "to return to research")
s6 = Student("Jessica","​Jessi_RS [Gold]", "pasta", "work as developer by end of the year")
s7 = Student("Bituin Callanta","​bituin [gold]", "sashimi", "lessen the gender wage gap")

# s1.my_print()
# s1.fav_food = "ice cream"
# s1.my_print()

# #you can delete properties but they will error out

class Ideal_Student():
	def __init__(self, first_name, last_name, email, country_code, phone, github, country, identity, goal, coding_level, group, help_out):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.country_code = country_code
		self.phone = phone
		self.github = github
		self.country = country
		self.identity = identity
		self.goal = goal
		self.coding_level = coding_level
		self.group = group
		self.help_out = help_out
	def my_print(self):
		print(self.first_name + " " + self.last_name + " " + self.email + " " + self.country_code " " + self.phone + " " + self.github + " " 
			+ self.country + " " + self.identity + " "	+ self.identity + " " + self.goal + " " + self.coding_level + " " + 
			self.group + " " + self.help_out + " ")