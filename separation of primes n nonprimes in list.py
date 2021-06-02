import math as m
def isprime(n):
    if n==1:
        return 0
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def findprimes(n,data):
    primes=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            primes.append(i)
        else:
            nonprimes.append(i)
            
    return *primes,nonprimes
            
n=int(input())
data=list(map(int,input().split()))
print(*findprimes(n,data))
