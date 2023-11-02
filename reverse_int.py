a=int(input("Enter the number:"))
b=str(a)
c=""
l=len(b)-1
for i in range(len(b)):
    c+=b[l]
    l-=1
print("The reversed int number is :",c)
