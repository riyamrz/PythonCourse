#wap that inputs cp and sp and determines whether the transaction is profit or loss

cp=int(input("Enter cost price: "))
sp=int(input("Enter selling price: "))

if cp>sp:
    print("The transaction is loss")
else:
    print("The transaction is profit")
    