box=[0]
count=0
k=1
for i in range(1,1001):
    box.append(k)
    count+=1
    if count==k:
        k+=1
        count=0
    box[i]+=box[i-1]

A,B=map(int,input().split())
print(box[B]-box[A-1])
