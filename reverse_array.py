def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i=0
    while (d<l):
       arr[i]=arr[d]
       i+=1
       d+=1
    arr[:]=arr[:i]+temp
    return arr
arr=[1,2,3,4,5]
d=2
l=len(arr)
print(rotateArray(arr,l,d))