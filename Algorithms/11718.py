final=[]
while True:
	try:
		final.append(input())
	except EOFError:
		break

for i in final:
	print(i)
