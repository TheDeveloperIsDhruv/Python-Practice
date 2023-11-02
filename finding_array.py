from operator import truediv


def missing(arr,a):
    if (a in arr):
        return True
    else:
        return False

a=int(input("Enter number:"))
arr=[1,2,3,4,5,6,7,8,9,10]
print(a,"is present ->",missing(arr,a))
    

