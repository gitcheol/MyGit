import sys 

N, M = map(int, sys.stdin.readline().split())

ans = 0 

not_case = [[0 for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    not_case[x][y] = 1 
    not_case[y][x] = 1 

# all_case
for i in range(1,N-1):
    for j in range(i+1,N):
        if not_case[i][j]:
            continue
        for k in range(j+1,N+1):
            if not_case[i][k] or not_case[j][k]:
                continue
            ans+=1
print(ans)
