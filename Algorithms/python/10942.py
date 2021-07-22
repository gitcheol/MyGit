import sys
N=int(sys.stdin.readline())

bag=list(map(int,sys.stdin.readline().split()))
bag.insert(0,0)

ans=""

M=int(input())
for _ in range(M):
   i,j=map(int,sys.stdin.readline().split())
   tmp=[]
   tmp=bag[i:j+1]
   if tmp==tmp[::-1]:
       ans+=(str(1)+'\n')
   else: ans+=(str(0)+'\n')

print(ans)
