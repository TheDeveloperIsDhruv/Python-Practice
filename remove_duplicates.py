a=[11,22,33,11,33,44,55]
b=[]
for i in a:
   if i not in b:
       b.append(i)
print("The duplicates have been removed",b)