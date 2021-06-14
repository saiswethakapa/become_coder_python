#left rotate alist by d positions
def rotate(n,d,arr):
    for j in range(d):
        for i in range(n-1):
            arr[i],arr[i+1]=arr[i+1],arr[i]
n=int(input())
d=int(input())
arr=list(map(int,input().split()))
rotate(n,d,arr)
print(arr)
