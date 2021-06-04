# no of numbers in org position in sorted list
def opo(n,data):
    a=list(set(data))
    a.sort()
    c=0
    for i in range(len(a)):
        if data[i]==a[i]:
            c=c+1
    return c
n=int(input())
data=list(map(int,input().split()))
print(opo(n,data))
