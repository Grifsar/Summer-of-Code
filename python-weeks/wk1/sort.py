print("Please enter as many words as you like and I will sort them for you. Press enter when you are done. ")
all_user_input = []
new_user_input = input("Please enter your first word, or hit enter to stop. ")

while new_user_input != "":
	all_user_input.append(new_user_input)
	new_user_input = input("Please enter a word, or hit enter to stop. ")

all_user_input.sort()
print(all_user_input)