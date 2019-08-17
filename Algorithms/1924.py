x,y=map(int,input().split())
a,b=1,1
c=0 

con1=[1,3,5,7,8,10,12]
con2=[4,6,9,11]
con3=[2]

for i in range(1,x):
	if i in con1:
		c+=31
	elif i in con2 :
		c+=30
	elif i in con3 :
		c+=28

c+=y

ans=c%7

if ans==1 :
	print("MON")
elif ans==2 :
	print("TUE")
elif ans==3 :
	print("WED")
elif ans==4 :
	print("THU")
elif ans==5 :
	print("FRI")
elif ans==6 :
	print("SAT")
elif ans==0 :
	print("SUN")

