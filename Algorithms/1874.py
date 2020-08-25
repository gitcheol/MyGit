a = int(input())
b = []
for i in range(a):
    b.append(int(input()))

result = []
final = []

for i in range(a):
    result.append(i+1)
    final.append('+')
    while True:
        if b[0] == result[-1]:
            del b[0]
            del result[-1]
            final.append('-')
            if len(b) == 0:
                break
            if len(result) == 0:
                break
        else:
            break

if len(b) == 0:
    for i in final:
        print(i)
else:
    print('NO')
