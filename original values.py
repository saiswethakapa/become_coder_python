def org(n,data):
    a=[]
    for i in data:
        if i not in a:
            a.append(i)
    return a
n=int(input())
data=list(map(int,input().split()))
print(*org(n,data))
