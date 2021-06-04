#how many numbers are in original position if the numbers are cosidered only once in list
def orgposition(n,data):
    a=[]
    c=0
    for i in data:
        if i not in a:
            a.append(i)
    for i in range(len(a)):
        if data[i]==a[i]:
            c=c+1
    return c
n=int(input())
data=list(map(int,input().split()))
print(orgposition(n,data))
