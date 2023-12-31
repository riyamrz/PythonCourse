principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate:"))
time=float(input("Enter the time:"))

interest=principal*(1+rate/100)**time - principal

print("Compound interest: ",interest)
