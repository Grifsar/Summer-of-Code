import to_eng
#import to_eng as tg

to_eng.to_eng(4)

c = to_eng.awesome_student["city"]

print(c)

import platform 

p = platform.system()
print(p)

#This lets you create files and directories
#import os

#let's you peak inside a module
d = dir(platform)
print(d)

#Let's you not use module.function to use functions in that module
from to_eng import to_eng
to_eng(5)