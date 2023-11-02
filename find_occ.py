a=input("Enter the string: ")
st=input("Enter the substring to be replaced: ")
c=0
for i in range(c,len(a)):
   if (a.startswith(st,i)):
       c+=1
print("The count is ",c)