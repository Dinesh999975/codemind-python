n=int(input())
d=list(map(int,input().split()))
s=9999
for i in d:
    if i<s:
        s=i
print(s)