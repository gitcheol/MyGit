s=input()
num=[]
for i in s:
    num.append(ord(i)-97)
x=num.copy()
x=sorted(x)
min1=s[num.index(x[0])]
min2=s[num.index(x[1])]
print(s)
print(min1,min2)


