T=int(input())
A=[[0 for col in range(31)] for row in range(31)]
for i in range(31):
    A[0][i]=1
for i in range(1,31):
    for j in range(1,31):
        A[i][j]=A[i-1][j-1]+A[i][j-1]
for _ in range(T):
    N,M=map(int,input().split())
    print(A[N][M])
