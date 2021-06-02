def reverse(data):
    rn=0
    a=[]
    for i in data:
        while i:
            r=i%10
            i=i//10
            rn=rn*10+r
        a.append(rn)
        rn=0
    return a
n=int(input())
data=list(map(int,input().split()))
print(*reverse(data))       
            
