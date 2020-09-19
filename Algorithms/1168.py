N,K=map(int,input().split())
K-=1

s=[]
for i in range(1,N+1):
    s.append(i)
ans=[]

length=len(s)

tmp=0
count=0

if K==0:
    s='<'
    for i in range(1,N+1):
        s=s+str(i)
        if i==N:
            break
        s+=','
    s+='>'
    print(s)
    exit()

ss='<'
while length:
    if tmp>=length:
        tmp=0
    if count==K:
        val=s.pop(tmp)
        length-=1
        if tmp>=length:
            tmp=0
        #ans.append(val)
        ss+=(str(val)+', ')
        count=0
    count+=1    
    tmp+=1 
    
ss=ss[0:-2]+'>'
print(ss)    
#print('<',end='')
#print(', '.join(list(map(str,ans))),end='')
#print('>')
