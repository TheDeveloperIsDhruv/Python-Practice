

from time import sleep


def setHours():
    c=int(input("Enter hours:"))
    return c
def setMinutes():
    b=int(input("Enter Minutes:"))
    return b
def setSeconds():
    a=int(input("Enter Seconds:"))
    return a

def printclock(h,m,s):
     if (h>24 or s>60 or m>60):
                print("Entered Wrong Time")
     else:
         while(True):
                if (s<=59):
                    s+=1
                if (m<59 and s==60):
                    m+=1
                    s=0
                if (m==59 and s==60):
                    h+=1
                    m=0
                    s=0
                if (h==24):
                    h=0
                    m=0
                    s=0
                else:
                    s+=0
                print(h,":",m,":",s)
                sleep(1)        

if __name__=="__main__":
    h1=setHours()
    m1=setMinutes()
    s1=setSeconds()
    print('\n')
    print("Set time as:",h1,":",m1,":",s1)
    print('\n')
    print("Clock Starts:")
    print('\n')
    printclock(h1,m1,s1)