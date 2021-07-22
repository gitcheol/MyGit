N,M=map(int,input().split())
A=[]
for i in range(M):
    A.append(int(input()))
A=sorted(A)
profit=0
max_profit=0

for i in range(M):
    if M-i<=N:
        profit=A[i]*(M-i)
    else:
        profit=A[i]*N
        
    if max_profit<profit:
        max_profit=profit
        price=A[i]

print(price,max_profit)
    
