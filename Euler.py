from math import *

count = 0
y0 = 0
x0 = 0
h = 0.1
second2last = -9999

while (round(y0, 4) != round(second2last, 4)):
    x1 = 0
    second2last = y0
    x0, y0 = 0, 0
    h = h / 10
    while (x1 < 2 - h/2):
        y1 = y0 + h * (x0**2 + y0**2 -3)
        x1 = x0 + h
        
        y0 = y1
        x0 = x1
    #h = h / 10
    
print(f"x: {x0 - h}, y: {y0:.7f}, step: {h}")