def solution(orders, course):
    candidate=[]
    x=[]*len(orders)
    for i in range(len(orders)):
        x.append(list(orders[i]))
    
    for i in range(len(x)):
        a=set(x[i])
        for j in range(i+1,len(x)):
            b=set(x[j])      
            
            candidate.append(a&b)
    
    print(candidate)
    tmp=candidate.copy()
    for i in candidate:
        if len(i)==1:
            tmp.remove(i) 
    
    #print(len(candidate))
    tmp.clear()
    
    answer=[]
    ans=[]
    for length in course:
        answer=[]
        tmp=[]
        for i in range(len(candidate)):
            if length==len(candidate[i]):
                tmp.append(list(candidate[i]))      
        #tmp에서 가장 개수가 많은 애들 =answer에 추가 
        
        ma=0
        for i in range(len(tmp)):
            val=tmp.count(tmp[i])
            if ma<val:
                ma=val
        for i in range(len(tmp)):
            if tmp.count(tmp[i])==ma:
                answer.append(''.join(tmp[i])) 

        tmp2=set(answer)
        tmp2=list(tmp2)
        for i in range(len(tmp2)):
            ans.append(tmp2[i])


    anss=[]
    for i in range(len(ans)):
        s=ans[i]     
        anss.append(''.join(sorted(s)))
        
    anss.sort()
    print(anss)


    return anss














menu=input().split()
course=list(map(int,input().split()))
solution(menu,course)

