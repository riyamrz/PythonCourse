#palindrome number

def palindrome(n): #function to check palindrome
    n = str(n) #converting number to string
    if n == n[::-1]: #checking if number is equal to its reverse
        return True
    else:
        return False
    
n = int(input("Enter a number:"))
if palindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")


