A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)
#print(A+B+C)

for i in range(0,B):
	A*=A

print(A%C)
