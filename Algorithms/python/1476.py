E,S,M=map(int,input().split())
a,b,c=1,1,1
now=1

while True:
	if a==E and b==S and c==M:
		break
	a+=1;b+=1;c+=1;now+=1
	if a==16:a=1
	if b==29:b=1
	if c==20:c=1

print(now)
