N=int(input())
move=list(input())

miro=[[0 for i in range(200)]for i in range(200)]

x,y=100,100
miro[x][y]='.'

x_t,x_b,y_t,y_b=100,100,100,100

m=0
for i in move:
    if i=='R':
        m+=1
        m%=4
    elif i=='L':
        m-=1
        m%=4

    if i=='F':
        if m==0:
            y+=1
            x_t+=1
        elif m==1:
            x-=1
            y_b-=1
        elif m==2:
            y-=1
            x_b-=1
        elif m==3:
            x+=1
            y_t+=1
            
        miro[x][y]='.'

#print(x_b,x_t)
#print(y_b,y_t)

for i in range(x_b+1,x_t+2):
    for j in range(y_b-1,y_t):
        if miro[i][j]==0:
            print('#',end='')
        else :
            print(miro[i][j],end='')

    print()





'''
ans=[]
flag=0
for i in range(200):
    for j in range(200):
        if miro[i][j]=='.':
            print('.',end='')
            flag=1 
    if flag:
        print()
        flag=0
'''     
