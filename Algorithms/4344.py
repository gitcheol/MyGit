C=int(input())

for i in range(C):
	a=list(map(int,input().split()))
	ave=((sum(a)-a[0])/a[0])
	pe=0
	for i in range(1,a[0]+1):
		if a[i]>ave:
			pe+=1
		
	ans=pe/a[0]*100
	print('%.3f%%' %ans)
