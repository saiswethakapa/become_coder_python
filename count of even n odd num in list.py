def even_odd(n,data):
    e,o=0,0
    for i in range(n):
        if data[i]%2==0:
            e=e+1
        else:
            o=o+1
    return (e,o)
n=int(input())
data=list(map(int,input().split()))
print(*even_odd(n,data))
