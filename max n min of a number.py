#minimum and maximum of a number 
n=int(input())
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
