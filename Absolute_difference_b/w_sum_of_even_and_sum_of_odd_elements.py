n=int(input())
d=list(map(int,input().split()))
even=0
odd=0
for i in d:
    if i%2==0:
        even+=i
    else:
        odd+=i
if(even>odd):
    dif=even-odd
else:
    dif=odd-even
print(dif)