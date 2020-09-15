count=1
while True:
    n=int(input())
    if n==0:
        break
    p=['name']
    for _ in range(n):
        p.append(input())
    
    check=[]
    for _ in range(2*n-1):
        i,j=input().split()
        i=int(i)
        check.append(i)
    for i in range(1,n+1):
        if check.count(i)==1:
            print(count,p[i])
            count+=1
            break
