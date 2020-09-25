N,score,P=map(int,input().split())

if N==0:
    print(-1)
    exit()

s=list(map(int,input().split()))

ranking=1

idx=len(s)-1
for i in range(N):
    if s[i]>score:
        ranking+=1
    if ranking==P:
        idx=i
        break

if s[idx]>=score:
    #if s[idx]>score and idx<N:
    #    print(ranking)
    #   exit()
    
    print(-1)
    exit()

print(ranking)
