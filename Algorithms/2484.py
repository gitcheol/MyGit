N=int(input())

ans=0

for _ in range(N):
    s=sorted(list(map(int,input().split())))
    ss=set(s)
    cash=0
    if len(ss)==1:
        cash=50000+s[0]*5000
    elif len(ss)==4:
        cash=max(s)*100
    elif len(ss)==3:
        if s[0]==s[1]:
            cash=1000+(s[0]*100)
        elif s[1]==s[2]:
            cash=1000+(s[1]*100)
        elif s[2]==s[3]:
            cash=1000+(s[2]*100)
    else:
        if s[0]==s[1] and s[2]==s[3]:
            cash=2000+(500*s[0])+(500*s[2])
        else : 
            if s[0]==s[1]:
                cash=10000+(s[0]*1000)
            elif s[2]==s[3]:
                cash=10000+(s[2]*1000)
            

    print(cash)
    if ans < cash : 
        ans=cash

    
print(ans)
    
