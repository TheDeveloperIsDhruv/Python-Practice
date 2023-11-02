a=int(input("Enter the number: "))
s=""
while (a!=0):
    s+=str(a%2)
    a=a//2
print(s)
