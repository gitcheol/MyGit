import numpy as np
N,r,c=map(int,input().split())

a=N
x=0

box = [[0 for col in range(2**N)] for row in range(2**N)]

def show(x,y):
    for i in range(2**y):
        for j in range(2**y):
            print('{0: >3}'.format(x[i][j]),end=' ')
        print()
 
def lot(N,i,j,box):
    global x
    global a
    if N==0:
        return 0
    if N==1:
        box[i-2][j-2]=x
        box[i-2][j-1]=x+1
        box[i-1][j-2]=x+2
        box[i-1][j-1]=x+3
        x+=4

    print('N : ',N,'i : ',i,'j : ',j)
    show(box,a)
    next_i=int(i/2)
    next_j=int(j/2)
    return lot(N-1,next_i,next_j,box)+lot(N-1,next_i,j,box)+lot(N-1,i,next_j,box)+lot(N-1,i,j,box)




lot(N,2**N,2**N,box)
show(box,N)
