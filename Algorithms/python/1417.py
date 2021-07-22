N=int(input())

v=[]
for _ in range(N):
    v.append(int(input()))

p=v[0]
tmp=v[0]
v[0]=0
while True:
    if p>max(v):
        break
    v[v.index(max(v))]-=1
    p+=1

print(p-tmp)        
