
import math 

h = int(input())
theta = int(input())
b = 0

if h<100 and (theta==30 or theta==45 or theta==60):
    hyp = h/math.cos(math.radians(theta))
    b = math.sin(math.radians(theta))*hyp
    print(math.floor(3.14*(b**2)))
else:
    print("Invalid input")