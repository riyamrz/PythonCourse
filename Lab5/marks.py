arr=[]

for x in range(5):
    marks=int(input("Enter your marks:"))
    arr.append(marks)

arr.sort()

print("Lowest marks: ",arr[0])
print("Highest marks: ",arr[4])