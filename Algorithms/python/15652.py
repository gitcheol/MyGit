N, M = map(int, input().split())
out =[]

def sol(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        sol(depth+1, i, N, M)
        out.pop()


sol(0, 0, N, M)
