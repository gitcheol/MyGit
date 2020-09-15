s=input()
ans=0
count=0
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(len(s)):
    if i+1!=len(s):
        if s[i]+s[i+1] in croatia:
            count+=1

    if i+2<len(s):
        if s[i]+s[i+1]+s[i+2] == croatia:
            count+=1
print(len(s)-count)
