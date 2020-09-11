N,M=map(int,input().split())
A=set()
B=set()
for _ in range(N):
    A.add(input())
for _ in range(M):
    B.add(input())
C=A&B
C=sorted(C)
print(len(C))
print('\n'.join(C))
    
    

