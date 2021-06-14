#leaders of the list            
def leader(n,arr):
    for i in range(n-1):
        if arr[i]==max(arr[i:n]):
            a.append(arr[i])

n=int(input())
a=[]
arr=list(map(int,input().split()))
print(leader(n,arr))
print(*a)
