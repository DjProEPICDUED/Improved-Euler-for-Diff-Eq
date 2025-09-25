Adaptive Improved Euler Method ODE Solver
TLDR
A Python solution for a first-order ordinary differential equation (ODE) of the form y' = f(x, y). This script uses the Improved Euler method (also known as Heun's method), which is a second-order Runge-Kutta method, to approximate the solution.

TLDR ON HOW TO USE
You will need to manually change the code to input the Differential Equation. The program takes in the x-coordinate you want to get to, the initial y-value, the initial x-value, the starting step size (h), and the desired tolerance for accuracy.

Features
Improved Euler (Heun's) Method: Implements a second-order Runge-Kutta method for a more accurate approximation than the standard Euler method.

Adaptive Step Size: The script automatically refines the step size h by a factor of 10 in each iteration until the final result is stable within a user-defined tolerance.

User-Defined Precision: You can specify how accurate you want the final result to be by entering a number of decimal places for the tolerance check.

Customizable ODE: The differential equation y' = f(x, y) can be easily modified within the func(x, y) function to solve any first-order ODE.

How It Works
The script's logic is built on two nested loops:

The Outer while Loop: This loop controls the convergence. It continues to run as long as the absolute difference between the final y value from the current iteration and the previous iteration is greater than the specified tolerance. After each full run, it decreases the step size h by a factor of 10.

The Inner for Loop: This loop performs the core Improved Euler calculation for a given step size h. It iterates a precise number of times to step from the initial x0 to the final xfinal.

How to Use
1. Modify the ODE
Open the Python script and locate the func(x, y) function. Change the return statement to match the differential equation you want to solve. The default is set to y' = x² + y² - 1.

def func(x, y):
    # Change the equation below
    return x**2 + y**2 - 1

2. Run the Script
Execute the script from your terminal.

python your_script_name.py

3. Provide Inputs
The program will prompt you for the following information.

Final x: The x value for which you want to find y(x).

Starting step size: A starting h value (e.g., 0.1).

y0: The initial value for y.

x0: The initial value for x.

Tolerance: The number of decimal places of accuracy you want (e.g., 4 for a tolerance of 0.0001).

Example
To solve y' = x² + y² - 1 for y(1.5) with an initial condition of y(0) = 0 and accuracy to 4 decimal places:

Enter x: 1.5
Enter the starting step size: 0.1
Enter y0: 0
Enter x0: 0
Enter the number of decimal places you want it to be accurate to: 4

Output:

x: 1.5, y: -0.1415, 
Stoped at step: 0.0001
