n=int(input())
d=list(map(int,input().split()))
os=0
for i in range(0,n):
    s=d[i]
    s=int(s)
    if s%2!=0:
        os+=s
print(os)