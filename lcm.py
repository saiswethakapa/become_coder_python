a,b=map(int,input().split())
res,i=1,2
while i<=a or i<=b:
   if a%i==0 and b%i==0:
      res=res*i
      a=a//i
      b=b//i
   else:
      i=i+1
print(res*a*b)    
