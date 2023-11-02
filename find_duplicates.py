def find_duplicates(a):
    for i in range(len(a)):
        if (a.count(i)>1):
            return True

a=[1,2,3,4]
print(find_duplicates(a))