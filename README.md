Adaptive Improved Euler Method ODE Solver
Overview
This Python script provides a numerical solution to a first-order ordinary differential equation (ODE) of the form y' = f(x, y). It uses the Improved Euler method (also known as Heun's method), which is a second-order Runge-Kutta method, to approximate the solution.

A key feature of this script is its adaptive step size. It starts with an initial step size h and iteratively refines it by a factor of 10 until the final calculated value for y converges and is stable to a specified number of decimal places (currently 4). This ensures a balance between computational effort and the accuracy of the final result.

Features
Improved Euler Method: Implements Heun's method for a more accurate approximation than the standard Euler method.

Adaptive Step Size: Automatically reduces the step size h until the solution converges, ensuring reliable results.

User-Defined Inputs: Allows the user to specify the initial conditions (x0, y0), the final x value, and the starting step size.

Customizable ODE: The differential equation y' = f(x, y) can be easily modified within the func(x, y) function.

How to Use
Clone or download the repository.

Run the script from your terminal:

python your_script_name.py

Enter the required inputs when prompted:

The final x value for which you want to find y(x).

The starting step size h (e.g., 0.1).

The initial condition for y (y0).

The initial condition for x (x0).

The script will then run, iteratively reducing the step size, until the solution is stable. The final result and the step size that achieved it will be printed to the console.

Example
For the differential equation y' = x + 0.5 * y^2:

Enter the final x: 2
Enter the starting step size: 0.1
Enter y0: 0
Enter x0: -2

Output:

x: 2.0, y: 1.4633, step: 0.0001

Code Description
The core logic is contained within two nested while loops.

Outer Loop: This loop controls the adaptive step size. It continues to run as long as the final y value from the current iteration is different from the y value of the previous iteration (checked to 4 decimal places). At the end of each run, it reduces the step size h by a factor of 10.

Inner Loop: This loop performs the Improved Euler method calculation for a given step size h, starting from the initial conditions (x0, y0) and ending when x reaches xfinal.

The differential equation is defined in the func(x, y) function. By default, it is set to:
y' = x + 0.5 * y^2

You can modify the return statement in this function to solve any other first-order ODE.
