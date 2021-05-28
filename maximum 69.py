def si(n):
    temp=n
    ns,c1,dmc=0,0,0
    while n:
        r=n%10
        n=n//10
        c1=c1+1
        if r==6:
            ns=ns+1
            dmc=c1
    n=temp
    c2,nn,t=0,0,1
    while n:
        r=n%10
        n//=10
        c2=c2+1
        if r==6 and c2==dmc:
            r=9
        nn=nn+r*t
        t=t*10
    return nn
n=int(input())
print(si(n))
