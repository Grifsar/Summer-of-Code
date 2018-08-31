#Day 1
print("Day 1")
print("There are " + str(24 * 365) + " hours in a year")
print("There are " + str(60 *24 * 365 * 10) + " minutes in a decade")
print("I am " + str(60 * 60 *24 * 365 * 30 ) + " seconds old")
print("Andreea Visanoiu is " + str(48618000/60/60/24/365) + " years old?")
#I assume the rest is optional for this day...
#Day 2
#There wasn't a Things to Try section for Day 2 so I'm moving on

#Day 3
first_name = input("What is your first name? ")
middle_name = input("What is your middle name? ")
last_name = input("What is your last name? ")
print("Hello, " + first_name + " " + middle_name + " " + last_name + ". It's nice to meet you. \n")
favorite_number = input("What is your favorite number? ")
if(favorite_number.isnumeric()):
  print("That's a lovely number. I bet you'd love " + str(int(favorite_number) + 1) + ", which is the new and improved version of your favorite number.")
else:
  print("I'm sorry, but " + favorite_number + " isn't a number.\n")

you_said = input("Whaddaya want? ")
print("WHADDAYA MEAN \"" + you_said + "\"?!? YOU'RE FIRED!!\n")
print("Table of Contents\n")
print(("Chapter 1: Getting Started ").ljust(0) + (" page 1").rjust(0))
print(("Chapter 2: Numbers ").ljust(0) + (" page 9").rjust(15))
print(("Chapter 3: Letters ").ljust(0) + (" page 13").rjust(15)+"\n")

#Day 4

bottles = 99
bottles_word = " bottles"
while bottles > 0:
  print(str(bottles) + bottles_word + " of beer on the wall. \n" + str(bottles) + bottles_word + " of beer")
  bottles = bottles - 1
  print("Take one down, pass it around.")
  if bottles == 1:
    bottles_word = " bottle"
  if bottles == 0:
    print("No more bottles of beer on the wall. \n")
  else:
    print(str(bottles) + bottles_word + " of beer on the wall. \n")

import random
deaf_grandma = input("Grandma wants to know how you're doing. ")
bye_count = 0
while(bye_count != 2):
 if(deaf_grandma == "BYE" and bye_count < 2):
  deaf_grandma = input("WHAT WAS THAT? ")
  bye_count += 1
 elif(deaf_grandma.isupper()):
  print("No, not since " + str(random.randint(1930,1950)) + ".")
  deaf_grandma = input("HOW ARE YOU DOING? ")
  bye_count = 0
 else:
  deaf_grandma = input("HUH?! SPEAK UP, GIRL! " )
  bye_count = 0
print("BYE! PLEASE TALK TO ME AGAIN SOON!")

print("Let's calculate leap years. This program will check to see if the start year and the end year are leap years")
start_year = input("Please give me the first year ")
#check valid year function
def valid_year(checkYear):
 while(checkYear.isalpha()):
  checkYear = input("That is not a valid year. Please enter a valid year. ")
 return checkYear
start_year = valid_year(start_year)
end_year = input("Please give me the second year ")
end_year = valid_year(end_year)
while(int(end_year) <= int(start_year)):
 end_year = input("The ending year can't be before the starting year. ")
 end_year = valid_year(end_year)
current_year = int(start_year)
print("The following years are leap years:")
while(current_year <= int(end_year)):
  if(current_year%400 == 0):
   print(current_year)
   current_year+=1
  elif(current_year%4 == 0 and current_year%100 != 0):
   print(current_year)
   current_year+=1
  else:
   current_year+=1

print("Please enter as many words as you like and I will sort them for you. Press enter when you are done. ")
all_user_input = []
new_user_input = input("Please enter your first word, or hit enter to stop. ")

while new_user_input != "":
  all_user_input.append(new_user_input)
  new_user_input = input("Please enter a word, or hit enter to stop. ")

all_user_input.sort()
print(all_user_input)

contents = ["Chapter 1", " 1", "Chapter 2", "5", "Chapter 3", "6"]

c = 0
while c < len(contents) - 1:
  if c%2 == 0:
    print(str(contents[c]).ljust(0) + str(contents[c+1]).rjust(10) )
    c+=2

def say_moo(n):
  print("moo " * n)

say_moo(5)

number = input("Please enter a number. ")
while number.isalpha() == True:
  number = input("That isn't a number. Please enter a number. ")

def to_old_roman(n):
  if(int(n) == 0):
    return 0
  old_roman = ""
  if int(n)//1000 > 0:
    amount_m = int(n)//1000
    old_roman = old_roman + "M" * amount_m
    n = int(n) - int(amount_m)*1000
    to_old_roman(n)
  if int(n)//500 > 0:
    amount_d = int(n)//500
    old_roman = old_roman + "D" * amount_d
    n = int(n) - int(amount_d)*500
    to_old_roman(n)
  if int(n)//100 > 0:
    amount_c = int(n)//100
    old_roman = old_roman + "C" * amount_c
    n = int(n) - int(amount_c)*100
    to_old_roman(n)
  if int(n)//50 > 0:
    amount_l = int(n)//50
    old_roman = old_roman + "L" * amount_l
    n = int(n) - int(amount_l)*50
    to_old_roman(n)
  if int(n)//10 > 0:
    amount_x = int(n)//10
    old_roman = old_roman + "X" * amount_x
    n = int(n) - int(amount_x)*10
    to_old_roman(n)
  if int(n)//5 > 0:
    amount_v = int(n)//5
    old_roman = old_roman + "V" * amount_v
    n = int(n) - int(amount_v)*5
    to_old_roman(n)
  if int(n)//1 > 0:
    amount_i = int(n)//1
    old_roman = old_roman + "I" * amount_i
    n = int(n) - int(amount_i)*5
    to_old_roman(n)
  return old_roman

def to_new_roman(n):
  if(int(n) == 0):
    return 0
  new_roman = ""
  if int(n)//1000 > 0:
    amount_m = int(n)//1000
    new_roman = new_roman + "M" * amount_m
    n = int(n) - int(amount_m)*1000
    to_new_roman(n)
  if int(n)//900 > 0:
    amount_cm = int(n)//900
    new_roman = new_roman + "CM" * amount_cm
    n = int(n) - int(amount_cm)*900
    to_new_roman(n)
  if int(n)//500 > 0:
    amount_d = int(n)//500
    new_roman = new_roman + "D" * amount_d
    n = int(n) - int(amount_d)*500
    to_new_roman(n)
  if int(n)//400 > 0:
    amount_cd = int(n)//400
    new_roman = new_roman + "CD"
    n = int(n) - int(amount_cd)*400
    to_new_roman(n)
  if int(n)//100 > 0:
    amount_c = int(n)//100
    new_roman = new_roman + "C" * amount_c
    n = int(n) - int(amount_c)*100
    to_new_roman(n)
  if int(n)//90 > 0:
    amount_xc = int(n)//90
    new_roman = new_roman + "XC"
    n = int(n) - int(amount_xc)*90
    to_new_roman(n)
  if int(n)//50 > 0:
    amount_l = int(n)//50
    new_roman = new_roman + "L" * amount_l
    n = int(n) - int(amount_l)*50
    to_new_roman(n)
  if int(n)//40 > 0:
    amount_xl = int(n)//40
    new_roman = new_roman + "XL"
    n = int(n) - int(amount_xl)*40
    to_new_roman(n)
  if int(n)//10 > 0:
    amount_x = int(n)//10
    new_roman = new_roman + "X" * amount_x
    n = int(n) - int(amount_x)*10
    to_new_roman(n)
  if int(n)//9 > 0:
    amount_ix = int(n)//9
    new_roman = new_roman + "IX"
    n = int(n) - int(amount_ix)*9
    to_new_roman(n)
  if int(n)//5 > 0:
    amount_v = int(n)//5
    new_roman = new_roman + "V" * amount_v
    n = int(n) - int(amount_v)*5
    to_new_roman(n)
  if int(n)//4 > 0:
    amount_iv = int(n)//4
    new_roman = new_roman + "IV"
    n = int(n) - int(amount_iv)*4
    to_new_roman(n)
  if int(n)//1 > 0:
    amount_i = int(n)//1
    new_roman = new_roman + "I" * amount_i
    n = int(n) - int(amount_i)*5
    to_new_roman(n)
  return new_roman

print("The old roman numeral for that number is " + to_old_roman(number))
print("The new roman numeral for that number is " + to_new_roman(number))