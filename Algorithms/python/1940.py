N=int(input())
M=int(input())

s=list(map(int,input().split()))
s=set(s)

ans=0

for i in range(1,M):
    count=0
    if i in s :
        count+=1
    if M-i in s :
        count+=1 
    if count==2:
        ans+=1

print(int(ans/2))
