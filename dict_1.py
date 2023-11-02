dic={"1":"One",
"2":"Two",
"3":"Three",
"4":"Four"}
phone=input("Enter number:")
o=""
for i in phone:
    o+=dic.get(i,"NOT")
    o+=" "
print(o)