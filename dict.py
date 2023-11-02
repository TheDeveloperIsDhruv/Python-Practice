dic={}
for i in range(4):
    size=int(input("Enter the size: "))
    price=int(input("Enter the price: "))
    dic[size]=price
print(dic)
sum=0
x=dic.values()
print(x)
for i in x:
    sum+=i
print("The total cost is: ",sum)