A,B,N=map(int,input().split())
digit=-1
ans=''
while digit!=N:
    ans+=str((A//B)%10)
    tmp=A%B
    A=tmp*10
    digit+=1
print(ans[N])
print(ans)
        
