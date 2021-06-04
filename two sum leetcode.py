def index(t,num):
    for i in range(0,len(num)):
        for j in range(len(num)-1,i,-1):
            if num[i]+num[j]==t:
                return (i,j)
t=int(input())
num=list(map(int,input().split()))
print(index(t,num))
