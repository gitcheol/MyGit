N,K=map(int,input().split())

vehicles=[[0]*4]*N
ans=[0]*N

time=0;

#1.time 1.money 2.time 2.money 
for city in range(N):
    vehicles[city][0],vehicles[city][1],vehicles[city][2],vehicles[city][3]=map(int,input().split())
    if time < vehicle[city][ :  


'''
배열을 하나 선언해서, N번째 도시에서의
최대 모금액을 저장
각 도시별 최대 모금액을 저장해 보고, 
만약 다음 도시에서 K를 넘어서면, 전 도시의 최대 금액을 바꿔본다.
바꿔보고 전보다 크면 그게 이번 도시까지의 최대금액이 되고, 
이런 식으로 진행하면 풀 수 있다. 

입력을 받는다
두 개싀 수단 중 K보다 작다면, 더 큰 모금액을 받는 것을 선택한다.
time과, ans를 업데이트 해준다.
두 개의 수단 모두 K보다 크다면, 전에 있는 수에서 둘 중 하나를 선택한다



'''
