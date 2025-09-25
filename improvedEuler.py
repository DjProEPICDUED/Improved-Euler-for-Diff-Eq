from math import *

xfinal = float(input("Enter the final x: ")) 
h = float(input("Enter the starting step size: ")) 
y0 = float(input("Enter y0: "))
x0 = float(input("Enter x0: "))
y = y0
x = x0
k1 = 0.00
k2 = 0.00
k_avg = 0.00
tempy = 0.00
second2lastY = -999.67

def func(x, y):
    return x + (0.5 * (y**2))

while (round(second2lastY, 4) != round(y, 4)):
    second2lastY = y
    x = x0
    y = y0
    while (x < xfinal):
        k1 = func(x, y)
        tempy = y + h*k1
        k2 = func(x+h, tempy)
        k_avg = (k1 + k2)/2
        y = y + h*k_avg
        x += h
    h = h /10

print(f"x: {x}, y: {y}, step: {h}")