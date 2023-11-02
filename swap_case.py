s="sTrInG"
a=""
for i in range(len(s)):
    if (s[i].isupper()):
        a+=s[i].lower()
    if (s[i].islower()):
        a+=s[i].upper()
print("The new string",a)
