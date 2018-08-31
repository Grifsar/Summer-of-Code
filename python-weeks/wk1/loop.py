characters = ["Virginia Schmidt", "Helen Trackton", "Katherine Stone", "Colm", "Vanessa"]

usernames = [print(c) for c in characters]

usernames = [c+"@team member" for c in characters]
print(usernames)
usernames.sort()
print(usernames)