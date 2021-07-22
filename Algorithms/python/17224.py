N,L,K=map(int,input().split())


pro=[]
for _ in range(N):
    easy,hard=map(int,input().split())
    pro.append([easy,hard])

pro=sorted(pro,key=lambda x: x[0])
pro=sorted(pro,key=lambda x: x[1])

ans=0
e,h=0,0
solved=0

for i in range(N):
    if solved == K:
        break
    if pro[i][1]<=L:
        h+=1
        solved+=1
    elif pro[i][0]<=L : 
        e+=1
        solved+=1

print(e*100+h*140)
