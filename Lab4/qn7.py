#marks of students

sub1=float(input("Enter your marks in python:"))
sub2=float(input("Enter your marks in science:"))
sub3=float(input("Enter your marks in english:"))

average=(sub1+sub2+sub3)/3

if(average>=90):
    print("Grade A")
elif(average<90 and average>80):
    print("Grade B")
elif(average<80 and average>70):
    print("Grade C")
elif(average<70 and average>60):
    print("Grade D")
else:
    print("Fail")