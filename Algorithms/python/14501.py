N=int(input())

consult=[[0 for i in range(2)] for i in range(N+1)]
d=[0]*(N+2)

for i in range(1,N+1):
    x,y=map(int,input().split())
    consult[i][0]=x
    consult[i][1]=y    
         
result=0
for i in range(1,N+2):
    for j in range(1,i):
        d[i]=max(d[i],d[j])
        if j+consult[j][0]==i:
            d[i]= max(d[i],d[j]+consult[j][1])
     
    result = max(result,d[i])


print(result)
