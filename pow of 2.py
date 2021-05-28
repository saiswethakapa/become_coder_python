def ispow2(n):#32
    i=0
    while True:
        if n==2**i:
            return True
        if n<2**i:
            return False
        i=i+1
        
n=int(input())
print(ispow2(n))
