N,M = map(int,input().split())
print(N,M)

R=[[0]*M in range(N)]



for i in range(N):
    for j in range(M):
        print(R[i][j], end=' ')
    print()
