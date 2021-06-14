#highest altitudes
def ha(data):
    n=len(data)
    a=[0]
    for i in range(n):
        b=data[0:i+1]
        
        a.append(sum(b))
    return max(a)
data=list(map(int,input().split()))
print(ha(data))
