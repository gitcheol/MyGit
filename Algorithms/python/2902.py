S=input()

print(S[0],end='')
for i in range(len(S)):
	if S[i]=='-':
		print(S[i+1],end='')
