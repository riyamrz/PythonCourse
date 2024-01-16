#fibonacci series

terms=int(input("Enter the number of terms: "))
n1=0
n2=1
count=0

while(terms!=count):
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
        