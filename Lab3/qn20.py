#WAP to find the Roots of a Quadratic Equation

import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = b*b - 4*a*c

if(d==0):
    print("Roots are real and equal")
    r1 = -b/(2*a)
    print("Root1 = Root2 = ", r1)
    
elif(d>0):
    print("Roots are real and unequal")
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("Root1 = ", r1)
    print("Root2 = ", r2)
    
else:
    print("Roots are imaginary")
    r1 = -b/(2*a)
    r2 = math.sqrt(-d)/(2*a)
    print("Root1 = ", r1, "+", r2, "i")
    print("Root2 = ", r1, "-", r2, "i")
