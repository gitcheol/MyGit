def cal(x):
	Answer=0
	a=0
	b=0
	while x>=2:
		if(x%2==0):
			x/=2
			a+=1
		if(x%5==0):
			x/=5
			b+=1

	#if(a%2 and (b-2)%2 and == 0)
	#	x=x-d
	#elif()
	return a+b

T=int(input())
N=[]
for x in range(0,T):
	N.append(int(input()))
	#N.append(a)

for x in N:
	b = cal(x)
	print(x)
	print(b)


