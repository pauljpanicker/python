import math
import random
from time import perf_counter

name=input("enter the name").split(",")
og=[]
for x in name:
    if x not in og:
        og.append(x)
print("final result"+str(og) )
display1=random.sample(og,2)
def reverse(string):
    string=string[::-1]
    return string
print("winner",display1[0],"rev:",reverse(display1[0]))
print("winner",display1[1],"rev:",reverse(display1[1]))
l=len(og)
print("total participates",l)
print("square",round(math.sqrt(l)))


