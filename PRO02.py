#Program No 2: Compare Mathematical Expressions and Find Unknown Values
# Import required functions from the SymPy library
from sympy import symbols, Eq, solve, simplify

# Create a symbolic variable x
x = symbols('x')

# Define the left-hand side (LHS) of the equation
expr1 = 2 * x + 3

# Define the right-hand side (RHS) of the equation
expr2 = 11

# Form the equation: 2x + 3 = 11
equation = Eq(expr1, expr2)

# Solve the equation for x
solution = solve(equation, x)

# Display the equation
print("Equation:", equation)

# Display the value of x
print("Value of x:", solution[0])

# Define the first algebraic expression
a = x**2 + 2*x + 1

# Define the second algebraic expression
b = (x + 1)**2

# Check whether both expressions are mathematically equivalent
print("Are expressions equivalent?", simplify(a - b) == 0)
