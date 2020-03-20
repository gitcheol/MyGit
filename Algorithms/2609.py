N=list(map(int,input().split()))


if N[0]>N[1]:
    small=N[1]
else :
    small=N[0]
for i in range(1,small+1):
    if N[0]%i == 0 and N[1]%i==0:
        re=i

print(re)

N[0]/=re
N[1]/=re
print(int(N[0]*N[1]*re))


