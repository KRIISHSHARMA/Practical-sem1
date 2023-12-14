import math as m 
a= int(input("enter numerical coefficient 1 :  "))
b= int(input("enter numerical coefficient 2 :  "))
c= int(input("enter numerical coefficient 3 :  "))
# taking the discriminant 
discriminant = b ** 2 - 4 * a * c
# if d > 0 , roots are real and distinct
if discriminant > 0 :
    root1 = (-b + m.sqrt(discriminant)) / (2 * a)
    root2 = (-b - m.sqrt(discriminant)) / (2 * a)
    print("Roots are real and distinct")
    print("Root 1:", root1)
    print("Root 2:", root2)
# if d = 0 , roots are real and same
elif discriminant == 0:
    root = -b / (2 * a)
    print("Roots are real and same")
    print("Root:", root)
# if d < 0 , roots are complex and diffrent     
else:
    realPart = -b / (2 * a)
    imaginaryPart = m.sqrt(-discriminant) / (2 * a)
    print("Roots are complex and different")
    print("Root 1:", realPart, "+", imaginaryPart, "i")
    print("Root 2:", realPart, "-", imaginaryPart, "i")