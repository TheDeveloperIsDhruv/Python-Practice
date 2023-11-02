# Changing the character at a particukar position in python by coverting it to list
# Then converting it to string back from list
s=input("Enter the string:")
ch=input("Enter the index number and character to be inserted: ")
pos=int(ch[0])
l=list(s)
l[pos]=ch[2]
x="".join(l)
print(x)
print("abcdefg".join("'''"))