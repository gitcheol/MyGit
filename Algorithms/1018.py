N,M=map(int,input().split())
C=[]

for i in range(N):
	C.append(list(input()))	

min=1000000

for i in range(N-7):
	for j in range(M-7):
#print("here : ",i,' ',j)
		if C[i][j]=='W' or C[i][j]=='B':
			temp=0
			for x in range(8):
				for y in range(8):
					if (x+i)%2==0 and (y+j)%2==0:
						if C[x+i][y+j]=='B':
							temp+=1
					if (x+i)%2==0 and (y+j)%2==1:
						if C[x+i][y+j]=='W':
							temp+=1
					if (x+i)%2==1 and (y+j)%2==0:
						if C[x+i][y+j]=='W':
							temp+=1
					if (x+i)%2==1 and (y+j)%2==1:
						if C[x+i][y+j]=='B':
							temp+=1
#		print('up : ','i:  ',i,'j : ',j, 'temp : ',temp)
		if min>temp:
		   min=temp
		
		if C[i][j]=='B' or C[i][j]=='W':
			temp=0
			for x in range(8):
				for y in range(8):
#					print(x+i,' ',y+j)
					if (x+i)%2==0 and (y+j)%2==0:
						if C[x+i][y+j]=='W':
							temp+=1
					if (x+i)%2==0 and (y+j)%2==1:
						if C[x+i][y+j]=='B':
							temp+=1
					if (x+i)%2==1 and (y+j)%2==0:
						if C[x+i][y+j]=='B':
							temp+=1
					if (x+i)%2==1 and (y+j)%2==1:
						if C[x+i][y+j]=='W':
							temp+=1
#	print('i:  ',i,'j : ',j, 'temp : ',temp)
		if min>temp:
			min=temp

print(min)



'''
for i in range(N):
	for j in range(M):
		print(C[i][j],' ',end='')
	print("")
	'''
