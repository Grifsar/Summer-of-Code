name = "Rebecca Fillier"
i = 0
#for i in range(0, len(name)):
# print(name[i])
#prints every other letter
result = ""
for i in range(0, len(name)):
  if i % 2 == 0:
    result = result + name[i]
print("The final result is " + result)

response = input('How are you?')
print('You entered ' + response)