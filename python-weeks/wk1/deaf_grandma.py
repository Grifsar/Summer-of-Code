import random
#Day 4
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