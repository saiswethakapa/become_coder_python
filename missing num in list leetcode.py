def mn(data):
    data.sort()
    n=len(data)
    mi=min(data)
    ma=max(data)
    c=0
    if 0 in data:
        for i in range(mi,ma+1):
            if i not in data:
                return i
        c=c+1
        if c==n:
            return(ma+1)
    else:
        for i in range(mi,ma+1):
            if i not in data:
                return i
        c=c+1
        if c==n:
            return(mi-1)
    
data=list(map(int,input().split()))
print(mn(data))
