N=int(input())

N = set(input().split())

m=input()
M=input().split()

for i in M:
    if i in N :
        print(1)
    else :print(0)
