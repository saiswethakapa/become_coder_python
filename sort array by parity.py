#sort array by parity--leetcode
def sap(data):
    data.sort()
    print(data)
    for i in data:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    a.extend(e)
    a.extend(o)
    return a
data=list(map(int,input().split()))
e=[]
o=[]
a=[]
print(sap(data))
