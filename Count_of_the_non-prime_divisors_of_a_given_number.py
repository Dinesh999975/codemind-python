import math
def isprime(n):
    if n<2:
        return False
    sq=math.sqrt(n)
    sq=int(sq)
    for i in range(2,sq+1,1):
        if(n%i==0):
            return False
    return True
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        if(isprime(i)):
            continue
        else:
            c+=1
print(c)
        
