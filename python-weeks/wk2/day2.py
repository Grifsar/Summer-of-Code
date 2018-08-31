#print(chr(65))

M = 'land'
o = 'water'

#Should be 23
world = [[o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,o],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]

#should be 30
world_edge = [
 [o,o,o,o,M,o,o,o,o,o,o],
 [o,o,o,o,M,o,o,o,o,M,o],
 [o,o,o,o,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,M],
 [o,o,o,M,M,M,M,M,M,M,o],
 [o,o,o,o,o,o,M,M,M,o,o],
 [o,M,o,o,o,M,M,o,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,M,o,o,o,o,o]]

world_mono = [
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]]

def print_continent(world):
  i = 0
  square = 0
  for square in world[square][i]:
    print (world[i])
    i += 1
def reverse_print_continent(world):
  i = 0
  square = 0
  world.reverse()
  for square in world[square][i]:
    print (world[i])
    i += 1

def continent_counter(world, x, y): 
  if world[y][x] != 'land':
    return 0
  size = 1
  world[y][x] = 'counted land'

  #Row above
  iteration = 0
  area = 0
  for area in world:
    if(x-1 >= 0 and y-1 >= 0):
     size = size + continent_counter(world, x-1, y-1)
    if(x >= 0 and y-1 >= 0):  
     size = size + continent_counter(world, x , y-1)
    if(x+1 <= len(world) and y-1 >= 0):
     size = size + continent_counter(world, x+1, y-1)
    if(x-1 >= 0):
     size = size + continent_counter(world, x-1, y )
    if(x+1 <= len(world)):
     size = size + continent_counter(world, x+1, y )
    if(x-1 >= 0 and y+1 < len(world)):
     size = size + continent_counter(world, x-1, y+1)
    if(y+1 < len(world)):
     size = size + continent_counter(world, x , y+1)
    if(x+1 <= len(world) and y+1 < len(world)):
     size = size + continent_counter(world, x+1, y+1)
    iteration += 1
  return size
print_continent(world_edge)
print("Now in reverse")
reverse_print_continent(world_edge)
print(continent_counter(world_edge, 5, 5))


#33
#for i in range(65,65+2*26):
#   print(i, " stands for ", chr(i))

#Things to try
#for i in range(65,65+2*26):
#   if chr(i).isalpha():
#       print(i, " stands for ", chr(i))

#def print_alphabet():
#   for i in range(65,65+2*26):
#       if chr(i).isalpha():
#           print(i, " stands for ", chr(i))
#print("Now printing with the function")
#print_alphabet()

#convert_to_ascii = input("Please enter the phrase that you want converted to ascii. ")

#for l in convert_to_ascii:
#   print(ord(l))