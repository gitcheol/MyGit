N,K=map(int,input().split())

box=[]

for i in range(2,N+1):
    box.append(i)

count=0

while box:
    P=box[0]
    i=1
    while True:
        if P*i>N:
            break
        if P*i in box:
            box.remove(P*i)
            count+=1
            if(count==K):
                print(P*i)
                exit()
                
                
        i+=1

