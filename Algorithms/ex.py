number = int(input())

number2 = 0

참치 = []

for i in range(1, number + 1):
    Text = str(i)
    참치.extend(Text)

print(참치)
참치 = [참치 for 참치 in 참치]
print(참치)
number2 = 참치.count('3') + 참치.count('6') + 참치.count('9')

print(number2)
