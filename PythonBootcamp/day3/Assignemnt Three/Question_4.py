# Computing the Perimeter of a Triangle
#side1, side2, side3 = eval(int(input("Enter three edges: ")))
side1, side2, side3 = map(int, input("Enter three edges: ").split(","))
perimeter = side1 + side2 + side3
if (((side1 + side2) > side3) and ((side2 + side3) > side1) and ((side1 + side3) > side2)):
        print(f"The perimeter is {perimeter}")
else:
     print("The Input is invalid.") 