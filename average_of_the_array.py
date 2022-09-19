n=int(input())
d=list(map(int,input().split()))
s=0
c=0
for i in d:
    s+=i
avg=s/n
a="{:.2f}".format(avg)
print(a)