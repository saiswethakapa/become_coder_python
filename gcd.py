a,b=map(int,input().split())
if a>b:
   a,b=b,a
r=b%a
while r!=0:
      b=a
      a=r
      r=b%a
print(a)
