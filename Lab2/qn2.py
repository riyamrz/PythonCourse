#Write a program that prompts the user to enter number in two variables and swap the contents of the variables

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping: ")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping: ")
print("a =", a)
print("b =", b)
