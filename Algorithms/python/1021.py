N,M=map(int,input().split())

queue=[i for i in range(1,N+1)]
s=list(map(int,input().split()))

ans=[]
idx=0
count=0
while len(ans)!=M:
    if queue[0]==s[idx]:
        tmp=queue.pop(0)
        ans.append(tmp)
        idx+=1
        continue 

    case1=1 
    queue1=queue.copy()
    while True:
        tmp=queue1.pop()
        if tmp==s[idx]:
            break
        case1+=1
    
    case2=0 
    queue2=queue.copy()
    while True:
        tmp=queue2.pop(0)
        if tmp==s[idx]:
            break
        case2+=1

    value=min(case1,case2)
    count+=value
    if case1<case2:
        while case1:
            tmp=queue.pop()
            queue.insert(0,tmp)
            case1-=1
    else :
        while case2:
            tmp=queue.pop(0)
            queue.append(tmp)
            case2-=1
    
print(count)

 
