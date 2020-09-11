M=int(input())
N=int(input())
box=[1]*10001
box[0]=0
box[1]=0
for i in range(2,10001):
    for j in range(2,i):
        if i%j==0:
            box[i]=0
            break    
flag=True
x=0
y=0
for i in range(M,N+1):
    if box[i]==1:
        x+=i
        if flag==True:
            y=i
            flag=False

if flag==True:
    print(-1)
    exit()

print(x)
print(y) 
    
