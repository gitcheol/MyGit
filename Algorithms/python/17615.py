N=int(input())
X=list(input())


case1=0
case2=0
Y=X.copy()
R=X.count('R')


for i in range(N-1,N-1-R,-1):
    if X[i]=='B':
        tmp=i
        while(tmp>=0):
            tmp-=1
            if X[tmp]=='R':
                break
        X[i]='R'
        X[tmp]='B'
        case1+=1
        


R=X.count('B')
for i in range(N-1,N-1-R,-1):
    if X[i]=='R':
        tmp=i
        while(tmp>=0):
            tmp-=1
            if X[tmp]=='B':
                break
        X[i]='B'
        X[tmp]='R'
        case2+=1

if case1>case2:
    print(case2)
else : print(case1)
            
