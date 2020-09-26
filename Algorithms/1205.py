N,score,P=map(int,input().split())

if N==0:
    print(1)
    exit()

s=list(map(int,input().split()))

ranking=1

for i in range(len(s)):
    if s[i]>=score:
        ranking+=1


val=1
if ranking<=P:
    for i in range(len(s)):
        if s[i]>score:
            val+=1
        else :
            print(val)
            exit()
    print(ranking)
else : 
    print(-1)



