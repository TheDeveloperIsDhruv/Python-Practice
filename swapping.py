a=[1,2,3,4,5,6]
#swap by specific number
#Like swap 3 and 6
target=4
temp=3
for i in range(len(a)):
    if (a[i]==3):
        a[i]=target  
        i=i+1
    if (a[i]==4):
        a[i]=6
        i=i+1  
   
        
print("The temp is:",temp)
print("The new array is:",a)