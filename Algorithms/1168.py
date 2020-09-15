N,K=map(int,input().split())

s=[0]
for i in range(1,N+1):
    s.append(i)

ans=[]

tmp=1
while len(s)!=1:
    if tmp==K:
        ans.append(s[tmp])
        s[tmp+1]
        del s[tmp]
    tmp+=1
    if tmp==len(s):
        tmp=1    
    print(s)


print(ans)
