N=int(input())
A=list(map(int,input().split()))
B, C=map(int,input().split())

ans=0

for i in range(N):
    p=A[i]
    if p<=B:
        ans+=1
    else:
        ans+=1
        p-=B
        if p%C==0:
            ans+=p//C
        else :
            ans+=(p//C+1)
        



print(ans)
