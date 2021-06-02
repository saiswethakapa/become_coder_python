def palindrome(n):
    temp=n
    nn=0
    while n:
        r=n%10
        n//=10
        nn=nn*10+r
    if nn==temp:
        return 1
    else:
        return 0
    nn=0
def cop(data):
    c=0
    for i in data:
        if palindrome(i):
            c=c+1
    return c
n=int(input())
data=list(map(int,input().split()))
print(cop(data))
