def binary(a):
    t=""
    while a>0:
        t=t+str(a%2)
        a=a//2
    print("The binary conversion is",t)
a=int(input("Enter the number"))
binary(a)