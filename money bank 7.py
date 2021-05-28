def money(n):
    r=n%7
    q=n//7
    m,w=1,7
    sum=0
    for i in range(1,q+1):
        for j in range(m,w+1):
            sum=sum+j
        m=m+1
        w=w+1
    for k in range(m,m+r):
        sum=sum+k
    return(sum)
    
n=int(input())
print(money(n))
