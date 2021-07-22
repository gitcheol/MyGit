n=list(map(int,input().split()))
for i in range(min(n),1000000):
    count=0
    if i%n[0]==0:
        count+=1
    if i%n[1]==0:
        count+=1
    if i%n[2]==0:
        count+=1
    if i%n[3]==0:
        count+=1
    if i%n[4]==0:
        count+=1
    if count>=3:
        print(i)
        break 

