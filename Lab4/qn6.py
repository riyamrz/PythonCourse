weight=float(input("Enter your weight in kilogram:"))
height=float(input("Enter your height in meters:"))

index=weight/(height*height)
print("BMI:",index)

if(index<18.5):
    print("Underweight")
elif(index>=18.5 and index<=24.9):
    print("Normal")
elif(index>=25 and index<=29.5):
    print("Overweight")
else:
    print("Obesity")