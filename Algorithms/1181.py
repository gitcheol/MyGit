N=int(input())
word=[[] for i in range(51)]
for _ in range(N):
    s=input()
    length=len(s)
    word[length].append(s)
for i in range(51):
    if len(word[i]):
        tmp=set(word[i])
        word[i]=list(tmp)
        print('\n'.join(sorted(word[i])))

