import sys

N=int(input())
s=[]
for i in range(N):
    val=int(sys.stdin.readline())
    s.append(val)

s=sorted(s)

ans=4

for i in range(N):
    count=4
    k=1
    while k!=5:
        if i+k<N and s[i+k]-s[i]<5:
            count-=1
            k+=1    
        else:
            break   
        
    ans=min(ans,count) 

print(ans)
