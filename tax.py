a=int(input("Enter the price of bike"))
tax=0
if a > 100000:
     tax = 15/100*a
elif a >50000 and a <=100000:
     tax = 10/100*a
else:
     tax = 5/100*a
print("Tax to be paid ",tax)