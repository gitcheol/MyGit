a,b=map(int,input().split())
x,y=map(int,input().split())

ans=0
count=0


y+=x
y-=x











if a<x:
    a=y

for i in range(a,b+1):
    if i%x-y==0:
        count+=1
        ans=i
        i+=x
    if count==2:
        print('Unknwon Number')
        exit()

print(ans)

