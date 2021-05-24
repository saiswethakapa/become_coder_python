from math import *
def ispronic(n):
    a=int(sqrt(n))
    return n==a*(a+1)
n=int(input())
print(ispronic(n))
