def happy(n):
    if n==1:
        return True
    s=0
    while n:
        r=n%10
        n//=10
        s=s+(r**2)
    if s==1 or s==7:
        return True
    n=s
    if n>9:
        n=happy(n)
    return n==1
n=int(input())
print(happy(n))
