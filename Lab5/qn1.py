
length=int(input("Enter the length of array:"))

arr=[]

for x in range(length):
    num= int(input("Enter the values:"))
    arr.append(num)

arr.sort()

print("Largest number is ",arr[length-1])