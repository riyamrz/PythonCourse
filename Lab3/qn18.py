#WAP to check the alphabet or not.

ch = input("Enter a character: ")

if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch, "is an alphabet")
    
else:
    print(ch, "is not an alphabet")
    