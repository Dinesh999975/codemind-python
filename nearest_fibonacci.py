n=int(input())
a=0
b=1
s=[a,b]
i=3
while True:
    c=a+b
    s+=[c]
    if c>n:
        i=len(s)
        sc=s[i-2]
        sc=int(int(sc))
        d1=n-sc
        d2=c-n
        if d1==d2:
            print(sc,c)
            break
        if d1>d2:
            print(c)
            break
        else:
            print(sc)
            break
    a=b
    b=c
    i+=1