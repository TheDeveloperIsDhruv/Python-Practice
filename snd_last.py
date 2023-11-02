arr=[1,2,4,4,3]
m=[]
arr.sort()
print(arr)
l=arr[len(arr)-1]
print(l)
for i in range(len(arr)):
    if (arr[i]<l):
        m.append(arr[i])
print("The required array is",m)
print("So, the second last elemnt is",m[len(m)-1])
