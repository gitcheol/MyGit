N=int(input())
p=[]
for i in range(N):
    p.append(list(map(int,input().split())))
ans=[]
for i in range(N):
    count=1
    for j in range(N):
        if (p[i][0]<p[j][0] and p[i][1]<p[j][1]):
            count+=1
    print(count,end=' ')
