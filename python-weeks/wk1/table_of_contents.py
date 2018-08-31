contents = ["Chapter 1", " 1", "Chapter 2", "5", "Chapter 3", "6"]

c = 0
while c < len(contents) - 1:
	if c%2 == 0:
		print(str(contents[c]).ljust(0) + str(contents[c+1]).rjust(10) )
		c+=2