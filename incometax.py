income=float(input("Enter your income:"))
tax=0
if income<250000:
    print("NILL")
elif income<500000:
    new=income-25000
    tax=new*0.05
    print("Your tax:",tax)
elif income<1000000:
    new=income-500000
    tax=new*0.10
    print("Your tax:",tax)
elif income<1500000:
    new=income-1000000
    tax=new*0.15
    print("Your tax:",tax)
elif income>=1000000:
    new=income-1500000
    tax=new*0.20
    print("Your tax:",tax)
