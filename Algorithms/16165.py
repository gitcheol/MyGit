N,M= map(int,input().split())
team={}
for _ in range(N):
    team_name , num =input(), num=int(input())
    team_mem=[]
    for _ in range(num):
        team_mem.append(input())
    team[team_name]=team_mem
for _ in range(M):
    x, flage=input(), int(input())
    if flag : 
        for key in list(team.keys()):
            tmp=team.get(key)
            if x in tmp:
                print(key)
    else : 
        ans=team.get(x)
        print('\n'.join(sorted(ans)))
