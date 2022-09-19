n=int(input())
d=list(map(int,input().split()))
k=int(input())
c=0
for i in d:
    if i==k:
        c+=1
if c>0:
    print("True")
else:
    print("False")