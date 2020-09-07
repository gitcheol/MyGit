N=int(input())

s=input()
for _ in range(N-1):
    ss=input()
    for i in range(len(s)):
        if s[i]!=ss[i]:
            list_s=list(s)
            list_s[i]='?'
            s=''.join(list_s)

print(s)
