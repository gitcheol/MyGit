def makelotto():
	lotto=[];
	for i in range(0,6):
		i=randint(1,45)
		if i in lotto:
			continue
		lotto.append(i)


	return lotto
