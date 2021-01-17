N = int(input())
og_N = N 
ans = 0

while True:
    ans +=1
    
    first = (N%10)*10
    second = ((N//10) + (N%10))%10
    
    N = first + second 
    if og_N == N :
        break

print(ans)    
