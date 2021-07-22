s=[]
for i in range(8):
    s.append(int(input()))

ans1=sorted(s.copy())
print(sum(ans1[3:]))
ans2=[]
for i in range(3,8):
    ans2.append(s.index(ans1[i])+1)

ans2.sort()
print(' '.join(list(map(str,ans2))))

