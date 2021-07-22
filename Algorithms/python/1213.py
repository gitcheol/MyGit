s=input()
s=list(s)

ans=[]

if len(s)%2==0:
    for i in range(len(s)):
        if s.count(s[i])%2!=0:
            print("I'm Sorry Hansoo")
            exit()    
    s.sort()
    
    while s:
        front=s.pop()
        back=s.pop()
        ans.insert(0,front)
        ans.append(back)

else : 
    idx=0
    tmp=0
    for i in set(s):
        if s.count(i)%2==1:
            idx=s.index(i)
            tmp+=1
        if tmp==2:
            print("I'm Sorry Hansoo")
            exit()    
    
    ans.append(s.pop(idx))
    s.sort()

    while s:
        front=s.pop()
        back=s.pop()
        ans.insert(0,front)
        ans.append(back)
             
print(''.join(ans))
