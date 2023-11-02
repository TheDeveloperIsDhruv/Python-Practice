a=input("Enter the string: ")
b=True;c=True;d=True;e=True;f=True
for i in range(len(a)):
    if (a[i].isalnum):
        b=True
    if (a[i].isalpha):
        c=True 
    if (a[i].isdigit):
        d=True 
    if (a[i].islower):
        e=True
    if (a[i].isupper):
        f=True 
print(b,c,d,e,f)
