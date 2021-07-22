N=int(input())
s=int(N/5)
ans=s

while True:
	temp=N-5*s
	if temp<0 or s<0:
		print(-1)
		exit()
	if temp==0 or temp%3==0:
		break;
	s-=1 
	ans-=1

print(ans+int(temp/3))
