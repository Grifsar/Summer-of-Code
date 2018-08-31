filename = "alice_in_wonderland.txt"
file = open(filename, encoding='utf8')

#for line in file:
#	print(line)

raw = file.read()
#print(raw[:65])
print("The length of ALice in Wonderland is " + str(len(raw)))
result = []
from string import ascii_lowercase
for letter in ascii_lowercase:
	current_letter = 0
	current = 1
	while current <= len(raw):
		if raw[int(current):int(current+1)].isalph() and raw[int(current):int(current+1)].lower() == str(letter):
			current_letter += 1
		current += 1
	current_list = [str(letter), str(current_letter)]
	result.append(current_list)
	current_letter = 0
print(result)