a={"Ramji":[1,2,3,4],"Sitaji":99,"Lashmanji":99,"Hanumanji":99}
x="Ramji"
k=a.get(x)
print(k)
sum=0
for i in range(len(k)):
    sum+=k[i]
print("Average:",sum/len(k))