def check_prime(num):
    c=0
    for i in range(1,num):
        if (num%i==0):
                c+=1
    print("The count is:",c)
    if(c==1):
        print("Yes, it is prime")
    else:
        print("No, it is not a prime")

n=int(input("Enter the number:"))
check_prime(n)