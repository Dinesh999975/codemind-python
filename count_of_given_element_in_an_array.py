n=int(input())
d=list(map(int,input().split()))
l=int(input())
c=0
for i in d:
    if i==l:
        c=c+1
print(c)
    