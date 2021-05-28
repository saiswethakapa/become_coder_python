def pbs(l):
    s=0
    while l:
        r=l%2
        l//=2
        s=s+r
    return(s)
    
l=int(input())
print(pbs(l)
