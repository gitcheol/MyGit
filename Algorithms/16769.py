c1,m1=map(int,input().split())
c2,m2=map(int,input().split())
c3,m3=map(int,input().split())


for i in range(1,101):
    if i%3==1:
        milk=m1+m2
        if c2>=milk:
            m2=milk
            m1=0
        else:
            tmp=milk-c2
            m2=c2
            m1=tmp
    if i%3==2:
        milk=m2+m3
        if c3>=milk:
            m3=milk
            m2=0
        else:
            tmp=milk-c3
            m3=c3
            m2=tmp
    if i%3==0:
        milk=m3+m1
        if c1>=milk:
            m1=milk
            m3=0
        else:
            tmp=milk-c1
            m1=c1
            m3=tmp
            

print(m1)
print(m2)
print(m3)
