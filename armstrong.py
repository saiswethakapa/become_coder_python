n=int(input())#armstrong
temp=n
c=a=0
while n:#153
    r=n%10
    n=n//10
    c+=1
#print('no of digits=',c)
n=temp#153
while n:
    r=n%10
    n=n//10
    a=a+pow(r,c)
#print(a)
if a==temp:
    print('armstrong')
else:
    print('not armstrong')
