def ba(n):
    r1=n%2
    n=n//2
    while n:
        r=n%2
        n=n//2
        if r1==r:
            return False
        r1=r
        return True
n=int(input())
print(ba(n))
