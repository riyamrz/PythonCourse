# read price of 5 prod ani sum of all prod and find avg

arr=[]

length=int(input("Enter the length:"))

for x in range(length):
    num=int(input("Enter the price of product: "))
    arr.append(num)
    
print("Sum of product is ",sum(arr))
total=sum(arr)
avg=total/(length-1)
print("Average is ",avg)