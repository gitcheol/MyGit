K,R,N=input().split()
N=int(N)
def lo(a):
    s='0ABCDEFGH'
    y=s.index(a[0])
    x=int(a[1])
    return x,y
K=list(lo(K))
R=list(lo(R))

for _ in range(N):
    m=input()
    v=0
    h=0
    if 'B' in m:
        v-=1
    elif 'T' in m:
        v+=1
    if 'L' in m:
        h-=1
    elif 'R' in m:
        h+=1     
    before=K.copy()

    if (K[0]+v)<=8 and (K[0]+v)>=1 and (K[1]+h)<=8 and (K[1]+h)>=1:
        K[0]+=v
        K[1]+=h

    if K==R:
        if (R[0]+v)<=8 and (R[0]+v)>=1 and (R[1]+h)<=8 and (R[1]+h)>=1:
            R[0]+=v 
            R[1]+=h
        else : 
            K=before.copy()
s='0ABCDEFGH'
print(s[K[1]]+str(K[0]))
print(s[R[1]]+str(R[0]))
