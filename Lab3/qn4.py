age=int(input("Enter your age:"))

if(age<=12):
    print("Child")
elif(age>12 and age<19):
    print("Teenager")
elif(age>20 and age<59):
    print("Adult")
else:
    print("Senior Citizen")