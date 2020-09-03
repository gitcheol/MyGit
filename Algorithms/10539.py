N=int(input())
B=list(map(int,input().split()))

ans=[]
ans.append(B[0])
B.insert(0,0)

for n in range(2,N+1):
    ans.append(n*B[n]-sum(ans))


print(' '.join(list(map(str,ans))))
