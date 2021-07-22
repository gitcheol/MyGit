K,N=map(int,input().split())
bag=list(map(int,input().split()))

bag=sorted(bag)

x=[bag[0]]

tmp=[]


count=1

while count!=N:
    for i in range(len(bag)):
        for j in range(len(x)):
            val=bag[i]*x[j]
            tmp.append(val)
            if x[-1]<val:
                break
    tmp+=bag
    tmp=sorted(tmp)
    z=set(tmp)    
    y=set(x)
    z=z-y
    list_z=list(z)
    z=sorted(z)
    x.append(z[0])
    count+=1

print(x[-1])
           

  
