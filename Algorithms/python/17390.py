N=int(input())
S=list(input())
ans=0
bonus=0

for i in range(len(S)):
    score=i+1
    if S[i]=='O':
        ans+=score
        ans+=bonus
        bonus+=1
    else : 
        bonus=0

print(ans)    

