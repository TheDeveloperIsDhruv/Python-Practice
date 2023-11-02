s="ABCDEFGabcd"
a=""
for i in range(len(s)):
    if (i%4==0 and i!=0):
        print(a)
        a=s[i]
    else:
        a+=s[i]
print(a)