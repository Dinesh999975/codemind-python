def add(num):
    num=str(num)
    num1=list(map(int,num))
    s=sum(num1)
    return s
        
num=int(input())
res=add(num)
if res<10:
    print(res)
else:
    while res>=10:
        res=add(res)
    print(res)