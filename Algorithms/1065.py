N=int(input())
ans=0

for i in range(1,N+1):
	if i>=100 : 
		temp=str(i)
		a=int(temp[0])
		b=int(temp[1])
		c=int(temp[2])
		if b-a == c-b :
			ans+=1
	elif i>=10 : 
		ans+=1 
	else : ans+=1



print(ans)
