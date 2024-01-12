number = int(input("Enter the number: "))
n = 0
even = []
odd = []

while n <= number:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
    n += 1
    
# print ("Even= ",even)
# print("Odd= ",odd)

print("Even:")
for x in even:
    print(x)
    
print("Odd:")
for x in odd:
    print(x)