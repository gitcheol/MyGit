s=list(input())
ans=[]

count=0
for i in s:
    if i=='.':
        if count!=0:
            if count%2!=0:
                print(-1)
                exit()
            else:
                ans.append('AAAA'*(count//4)+'BB'*((count-4*(count//4))//2)) 
        count=0
        ans.append(i)
    if i=='X':
        count+=1

if count!=0:
    if count%2!=0:
        print(-1)
        exit()
    else:
        ans.append('AAAA'*(count//4)+'BB'*((count-4*(count//4))//2)) 

print(''.join(ans))




