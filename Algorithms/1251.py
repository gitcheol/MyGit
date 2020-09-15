s=list(input())
ans=[]

for i in range(len(s)):
    for j in range(i,len(s)):
        first=s[0:i]
        second=s[i:j]
        third=s[j:]
        if len(first)==0 or len(second)==0 or len(third)==0:
            continue
        ss=first[::-1]+second[::-1]+third[::-1]
        ans.append(''.join(ss))
        
print(min(ans))
