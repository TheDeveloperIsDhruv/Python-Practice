a=[["chi",20.0],["cd",49.0],["beta",50.0],["alpha",50.0]]
l=[]
m=[]
for i in range(len(a)):
    l.append(a[i][1])
print(l)
for j in range(len(l)-1):
    if(l[len(l)-1]>=l[j]):
        m.append(l[j])
print("The new required list is",m)
req=m[len(m)-1]
for k in range(len(a)):
    if (req==a[k][1]):
        print(a[k][0])