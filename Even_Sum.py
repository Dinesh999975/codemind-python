n=int(input())
d=list(map(int,input().split()))
k=0
for i in d:
    if i%2==0:
        k+=i
print(k)
        