#Write a program to generate fibonacci triangle.

n=int(input("Enter the number of rows: "))
a=0
b=1
c=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        a=b
        b=c
        c=a+b
    print()