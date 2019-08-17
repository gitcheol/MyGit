S=input()

B=[-1 for i in range(123)]
for i in range(len(S)):
	for j in range(97,123):
		if S[i]==chr(j):
			if B[j] != -1 : continue
			B[j]=i
			break

for i in range(97,123):
	print(B[i],end=' ')
