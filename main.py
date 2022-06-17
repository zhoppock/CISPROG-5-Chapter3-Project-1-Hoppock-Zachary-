#enter the lengths of 3 sides of a triangle
firstSide = int(input("Enter length of first side of triangle: "))
secondSide = int(input("Enter length of second side of triangle: "))
thirdSide = int(input("Enter length of third side of triangle: "))
#determine if the lengths of the sides make the triangle an equilateral triangle or not
if firstSide == secondSide and firstSide == thirdSide:
  print("This is an equilateral triangle!")
else:
  print("This is NOT an equilateral triangle.")