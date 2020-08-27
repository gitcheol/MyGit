n=int(input())

for _ in range(n):
    s=input()
    point=0
    pwd=[None]*(len(s)+1)

    for i in range(len(s)):
        if s[i]=='<' and point>0:
            point-=1
        elif s[i]=='>' and pwd[point]!=None:
            point+=1
        elif s[i]=='-' and point>0:
            point-=1
            del pwd[point]
        
        if s[i]!='<' and s[i]!='>' and s[i]!='-': 
            pwd.insert(point,s[i])
            point+=1
        #print("point : ",point,"  pwd :",pwd)

    ans = list(filter(None.__ne__, pwd))
    print(''.join(ans))
