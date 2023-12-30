physics= int (input("Enter your physics marks: "))
chemistry= int (input("Enter your chemistry marks: "))
maths= int (input("Enter your maths marks: "))
computer= int (input("Enter your computer marks: "))
english= int (input("Enter your english marks: "))

print("Your total marks is: ")
total= physics+chemistry+maths+computer+english
print(total)

print("Your percentage is: ")
percentage= total/500*100
print(percentage)

if(percentage>80):
    print("Distinction")
elif(percentage<80 and percentage>60):
    print("First Division")
elif(percentage<60 and percentage>50):
    print("Second Division")
elif(percentage<50 and percentage>40):
    print("Third Division")
else:
    print("Fail")



