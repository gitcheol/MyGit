import sys

def make_num(P):
    x=0
    for i in range(len(P)):
        x+=(P[len(P)-i-1]*(10**i))  
    return x 

N=int(input())
P=[int(i) for i in list(map(int,input().split()))]
ans=make_num(P)

if(sorted(P,reverse=True)==P):
    print(-1)
    sys.exit()

for i in range(N-1,0,-1):
    T=P.copy()
    for j in range(N-2,0,-1):
        tmp=T[j]
        T[j]=T[i]
        T[i]=tmp
        num=make_num(T)
        if num > ans:
            ans_list=list(str(num))
            for i in ans_list:
                print(int(i),end=' ')
            print()
            sys.exit()
        



#for i in ans:
#    print(i,end=' ')



