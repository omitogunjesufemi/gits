# Quadratic Equation
import math
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the value of the constant: "))

discriminant = ((b**2) - (4*a*c))
squareroot_discriminant = math.sqrt(discriminant)
xplus = ((b * (-1)) + (squareroot_discriminant)) / (2 * a)
xminus = ((b * (-1)) - (squareroot_discriminant)) / (2 * a)

if discriminant == 0:
    print(f"The root is {xplus:.4f} twice")

elif discriminant > 0:
    print(f"The root is {xplus:.4f} and {xminus:.4f}")

elif discriminant < 0:
    print(f"The root is a complex root")
