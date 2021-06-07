#finding the second largest number
def second_largest(data):
    a=data.copy()
    a.remove(max(data))
    return max(a)
data=list(map(int,input().split()))
print(second_largest(data))


#second largest value
def large(data):
    data.sort()
    data.reverse()
    print(data[1])
data=list(map(int,input().split()))
print(large(data))
