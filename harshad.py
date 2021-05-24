def hn(n):
    temp=n
    r,n,s=n%10,n//10,0
    s+=r
    return temp%s==0
n=int(input())
print(hn(n))
