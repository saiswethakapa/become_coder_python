def sp(n):
    p,a=1,0
    while n:
        r=n%10
        n=n//10
        p=p*r
        a=a+r
    return(p-a)
n=int(input())
print(sp(n))
