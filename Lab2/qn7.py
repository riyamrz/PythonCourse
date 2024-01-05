# WAP that asks your height in centimeters and converts it into foot and inches

height_cm = float(input("Enter your height in centimeters: "))
height_in = height_cm / 2.54
height_ft = height_in / 12

print("Your height in foot is", height_ft, "and inches is", height_in)
