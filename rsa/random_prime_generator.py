## probabilistic prime number generator using miller rabin (did 500 tests)
import random

def mypow(x,y,m):
    res=1
    x=x%m
    if x==0:
        return 0
    while y>0:
        if y&1:
            res=(res*x)%m
        y=y>>1
        x=(x*x)%m
    return res

def issprime(num,numtests=500):  # miller rabin
    if num==2:
        return True
    if num%2==0 or num<=1:
        return False
    s=0
    r=num-1
    while r&1==0:
        s+=1
        r=r//2
    for Y in range(numtests):
        a=random.randint(2,num-1)
        x=mypow(a,r,num)
        if x!=1 and x!=num-1:
            for j in range (1,s):
                if x==num-1:
                    break
                x=mypow(x,2,num)
                if x==1:
                    return False
            if x!=num-1:
                return False
    return True


def getTempPrime(length,isset):
    if length<100 or isset:
        p=random.getrandbits(length)
    else:
        tno=random.randint(length-20,length+20)
        p=random.getrandbits(tno)
    p|=((1<<(length-1))|1)      #setting msb and lsb to 1
    return p

def retPrime(length,isset):
    yy=4
    while issprime(yy)==False:
        yy=getTempPrime(length,isset)
    return yy
