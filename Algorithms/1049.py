N,M=map(int,input().split())

p=[0]*M
s=[0]*M

for i in range(M):
   p[i],s[i]=map(int,input().split())
   
p.sort()
s.sort()

flag=0
if p[0]/6 < s[0]:
    flag=1

if flag:
    case1=p[0]*(N//6)+s[0]*(N-(N//6)*6)
    case2=p[0]*(N//6+1)
    print(min(case1,case2))
else:
    print(s[0]*N)

