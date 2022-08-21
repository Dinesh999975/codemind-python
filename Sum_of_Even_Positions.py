n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=d[i]
    s=int(s)
    if i%2==0:
        c+=s
print(c)
