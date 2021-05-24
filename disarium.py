def dn(n):
    c=0
    temp=n
    while n:#175
        r=n%10
        n//=10
        c+=1
    n=temp
    s=0
    while n:
        r=n%10
        n//=10
        s=s+pow(r,c)
        c=c-1
    return temp==s
n=int(input())
print(dn(n))
