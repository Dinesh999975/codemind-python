n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(0,n):
    if d[i]%2!=0:
        c=i
print(c)