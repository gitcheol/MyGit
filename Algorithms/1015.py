N=int(input())
A=list(map(int,input().split()))
X=[]
B=sorted(list(A))
for i in range(N):
    idx=A.index(B[i])
    A[A.index(B[i])]=9999
    X.append(idx)
ans=[0]*N
for i in range(N):
    ans[X[i]]=i
print(' '.join(map(str,ans)))
