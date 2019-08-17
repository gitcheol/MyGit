T=int(input())

for i in range(T):
	S=input().split()
	S[0]=int(S[0])
	for j in range(len(S[1])):
		print(S[1][j]*S[0],end='')
	print("")
