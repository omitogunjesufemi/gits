# Computing the Volume and Area of a cylinder
radius = float(input("Enter the radius of the cylinder: "))
length = float(input("Enter the length of the cylinder: "))
area = radius ** 2 * (22/7)
volume = area * length
print(f"""
    The area of the cylinder is {area} 
    The volume of the cylinder is {volume}
""")