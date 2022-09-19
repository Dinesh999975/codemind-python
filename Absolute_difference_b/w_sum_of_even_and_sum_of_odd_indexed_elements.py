n=int(input())
d=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(d)):
    if i%2==0:
        even+=d[i]
    else:
        odd+=d[i]
if(even>odd):
    dif=even-odd
else:
    dif=odd-even
print(dif)