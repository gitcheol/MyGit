from random import *

def makelotto():
	lotto=set()
	while(len(lotto)<6):
		lotto.add(randint(1,45))
	return(list(lotto))

	return lotto

print(makelotto())
