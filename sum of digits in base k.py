def basek(n,k):
    c,s=1,0
    while n:
        r=n%k
        n=n//k
        s=s+r*c
        c=c*10
    sum=0
    while s:
        r=s%10
        s=s//10
        sum=sum+r
    return sum
n,k=map(int,input().split())
print(basek(n,k))

