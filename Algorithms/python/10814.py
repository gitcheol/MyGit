n = int(input())

a = []
for i in range(n):
    x, y = list(input().split())
    a.append((int(x), y))

b = sorted(a, key=lambda item: item[0])

for i in b:
    print(str(i[0]), i[1])
