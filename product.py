from itertools import product
#print(list(product([1,2,3],[3,4])))
#b=[[1,2,3],[3,4,5],[6,7]]
#print(list(product(*b)))
#A=[1,2,3]
#B=[4,5,6]
#print(list(product(A,B)))
a=input("Enter the list 1: ")
b=input("Enter the list 2: ")
l1=[]
l2=[]
for i in range(len(a)):
    if (a[i]!=" "):
        l1.append(int(a[i]))
for i in range(len(b)):
    if (b[i]!=" "):
        l2.append(int(b[i]))

print(list(product(l1,l2)))