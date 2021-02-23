N, M = map(int, input().split())

card = list(map(int, input().split()))

ans = min(card)

for i in range(N):
    for j in range(N):
        if i == j :
            continue
        for k in range(N):
            if i == k or j == k :
                continue
            tmp = card[i] + card[j] + card[k]
            if M-tmp >= 0 and ans < tmp:
                ans = tmp

print(ans)
