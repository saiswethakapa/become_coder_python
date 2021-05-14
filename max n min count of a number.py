#max n min count
n=int(input())#minimum and maximum of a number 
temp=n
max=a=b=0
min=9
while n:
    r=n%10
    n=n//10
    if r>max:
        max=r
    elif r<min:
        min=r
print('minimum=',min,'maximum=',max)
n=temp                   ###no of max and no of min<----
while n:
    r=n%10
    n//=10
    if r==min:
        a+=1
    elif r==max:
        b+=1
print('no of min=',a,'no of max=',b)

