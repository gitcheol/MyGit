L=int(input())
v=list(map(int,input().split()))
N=int(input())
v=sorted(v)
val=0
idx=0
for i in range(L):
    if v[i]==N:
        print(0)
        exit()
    if v[i]>N:
        val=v[i]-1
        idx=i
        break
ans=val-N
if v[0]>N:
    ans+=((v[0]-N)*(N-1))
if v[0]<N:
    ans+=((v[idx]-N)*(N-v[idx-1]-1))
print(ans)


