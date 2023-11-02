a=input("Enter the binary number:")
sum=0
b=0
j=len(a)-1
for i in range(len(a)):
    b=(2**i)
    sum+=b*int(a[j])
    j-=1
print(sum)