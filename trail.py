a=[1,2,3,3,2,1]
k=3
n=[]
c=0
for i in range(len(a)):
    if (a[i]!=k):
        n.append(a[i])
        c+=1
print("THe number of times the 3 is there =",len(a)-c)
for i in range(len(a)-c):
    n.append('_')
print(n)
    
        
