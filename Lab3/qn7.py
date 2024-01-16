#check prime number

num=int(input("Enter a number: "))

if num>1:
    for i in range(2,num): #range(2,num) means 2 to num-1
        if num%i==0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")