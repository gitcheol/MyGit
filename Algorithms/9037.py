T=int(input())

def sol(N,C):
    for idx,i in enumerate(C):
          if C[idx]%2==1:
              C[idx]+=1
    ans=0
    count=7
    while count:
        count-=1
        if C.count(C[0])==N:
            break  
        for i in range(len(C)):
            C[i]//=2
        x=[]
        x=C.copy()
        tmp=C[-1]
        C.insert(0,tmp)
        C.pop()
        #print('ans: ',ans, C)
        for i in range(len(C)):
            C[i]+=x[i]
        
        for idx,i in enumerate(C):
              if C[idx]%2==1:
                  C[idx]+=1
        #print('ans: ',ans, C)
        
        ans+=1 
    return ans







for _ in range(T):
    N=int(input())
    C=list(map(int,input().split()))
    ans=sol(N,C)
    print(ans)
