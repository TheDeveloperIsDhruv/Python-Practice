
list=[1]
n=int(input("Enter number of commands:"))
for i in range(n):
                cmd=input()
                if ("insert" in cmd):
                    index=int(cmd[7])
                    number=int(cmd[9])
                    list.insert(index,number)
                elif ("print" in cmd):
                    print(list)
                elif ("remove" in cmd):
                    a=int(cmd[7])
                    list.remove(a)
                elif ("append" in cmd):
                    number=int(cmd[7])
                    list.append(number)
                elif ("sort" in cmd):
                    list.sort()
                elif ("reverse" in cmd):
                    list.reverse()
                elif ("pop" in cmd):
                    list.pop()
