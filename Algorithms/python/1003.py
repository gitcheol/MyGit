T=int(input())

ans=[[1,0],[0,1],[1,1]]

for i in range(3,41):
    ans.append([ans[i-1][0]+ans[i-2][0],ans[i-1][1]+ans[i-2][1]])
    
for i in range(T):
    N=int(input())
    print(ans[N][0], ans[N][1])
