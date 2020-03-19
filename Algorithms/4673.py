def re(x):
    if x>10000: 
        return
    tmp=str(x)
    tmp=list(tmp)
    b=0
    for i in tmp:
        b+=int(i)       
    x=x+b
    if x<=10000:
        a[x]=1
    return re(x)



a=[0]*10001

for i in range(1,10001):
    re(i)

for i in range(1,10001):
    if a[i]==0:
        print(i)
   
