n=int(input())
d=list(map(int,input().split()))
s=0
c=0
for i in d:
    s+=i
avg=s//n
for k in d:
    if k==avg:
        c+=1
if c>0:
    print("True")
else:
    print("False")
    