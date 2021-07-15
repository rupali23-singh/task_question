purchased=int(input("enter the number"))
cost=purchased*100
if cost>1000:
    print(cost-cost*10/100)
else:
    print(cost)