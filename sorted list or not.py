def is_sorted(data):
    a=data.copy()
    a.sort()
    b=data.copy()
    b.sort() 
    b.reverse()
    if data==a or data==b:
        print('true')
    else:
        print(' False')

data=list(map(int,input().split()))
print(is_sorted(data))        
