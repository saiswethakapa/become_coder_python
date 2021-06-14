#ruuning sum
def running(arr):
    a=[]
    n=len(arr)
    for i in range(n):
        b=arr[0:i+1]
        s=sum(b)
        a.append(s)
    return a
    
arr=list(map(int,input().split()))
print(running(arr))
