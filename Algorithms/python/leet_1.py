s = input()
ans = 1
numbers = list(s)

if numbers[0]=='0': 
    print(0)
    exit()

for idx in range(len(s)-1):
    if numbers[idx] == '0':
        continue
    case = numbers[idx] + numbers[idx+1]
    if int(case)==10 or int(case)==20:
        continue
    if int(case) <= 26 :
        ans+=1


print(ans)
