def ac(n):
    i=0
    while n>0:
        i=i+1
        n=n-i
    if n==0:
        return i
    if n!=0:
        return i-1
n=int(input())
print(ac(n))
