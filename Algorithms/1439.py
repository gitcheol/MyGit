S=input()

ans=0
c=[S[0]]
val=S[0]
for i in range(1,len(S)):
    if val!=S[i]:
        val=S[i]
        c.append(val)

if c.count('0') > c.count('1'):
    print(c.count('1'))
else : print(c.count('0'))

