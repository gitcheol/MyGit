N = int(input())

p =[[0 for i in range(3)] for i in range(N)]

for idx in range(N):
    i,j,k = list(map(int, input().split()))
    p[idx][0], p[idx][1], p[idx][2] = i, j, k
    
ranking = sorted(p, key = lambda x : x[2], reverse=True)

country = [0]*1001

count = 0
idx = -1 

while count!=3:
    idx+=1
    country[ranking[idx][0]] +=1
    if country[ranking[idx][0]] == 3 :
        continue

    print(ranking[idx][0], ranking[idx][1])
    count+=1
