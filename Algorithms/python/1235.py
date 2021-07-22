N=int(input())
P=[]
for i in range(N):
    P.append(input())
length=len(P[0])
for i in range(-length,0,1):
    new=[]
    for s in P:
        tmp=s[i:]
        new.append(tmp)
    new=set(new)
    if len(new)!=N and i !=-length:
       print(-i+1)
       exit()
print(1)

