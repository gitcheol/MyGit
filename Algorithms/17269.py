N,M=map(int,input().split())
A,B=input().split()

def change(x):
    res=''
    alpha='32124313113132122212111221'
    for i in range(len(x)):
        tmp=ord(x[i])-65
        res+=alpha[tmp]
    return res    


x=change(A)
y=change(B)

length=0

if len(x)<len(y):
    length=len(x)
else :
    length=len(y)

s=''
for i in range(length):
    s+=x[i]
    s+=y[i]

if len(x)<len(y):
    s+=y[len(x):]
else :
    s+=x[len(y):]


bag=list(map(int,list(s)))

while len(bag)!=2:
    new=[]
    for i in range(0,len(bag)-1):
        val=bag[i]+bag[i+1]
        if val>=10:
            val-=10
        new.append(val) 
    bag=new


if bag[0]==0:
    print(str(bag[1])+'%')
    exit()
print(''.join(list(map(str,bag)))+'%')









