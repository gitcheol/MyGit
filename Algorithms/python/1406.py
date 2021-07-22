import sys

N=list(sys.stdin.readline().strip())
M=int(sys.stdin.readline())


length_N=len(N)
cursor=length_N

for _ in range(M):
    command=sys.stdin.readline().strip()
    
    if command[0]=='P':
        N.insert(cursor,command[2])
        cursor+=1
        length_N+=1
    elif command[0]=='L':
        if cursor!=0:
            cursor-=1
    elif command[0]=='D':
        if cursor!=length_N:
            cursor+=1
    elif command[0]=='B':
        if cursor!=0:
            del N[cursor-1]
            cursor-=1
            length_N=-1


print(''.join(N))
