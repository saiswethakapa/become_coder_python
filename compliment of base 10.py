def bitwiseComplement(n):
        if n==0:
            return 1
        b,c=0,1
        while n:
            r=n%2
            n=n//2
            if r==1:
                r=0
            else:
                r=1
            b=b+r*c
            c=c*10
        res,p=0,0
        while b:
            r=b%10
            b=b//10
            if r:
                res+=pow(2,p)
            p=p+1
        return res
n=int(input())
print(bitwiseComplement(n))
                
