N, M = map(int, input().split())

out=[]
def solv(depth, start, finish, N, M):
    if depth == M:
        print(' '.join(map(str,out)))
        return 

    for i in range(start, N):
        out.append(i+1)
        solv(depth+1, i, i+1, N, M)
        out.pop()

solv(0, 0, 0,N, M)


