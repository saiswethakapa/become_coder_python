def addDigits(num):
    if num<=9:
        return num
    if num>9:
        s=0
        while num:
            r=num%10  
            num//=10
            s=s+r
    num=s
    if num>9:
        num=addDigits(num)
    return num
num=int(input())
print(addDigits(num))
