N=int(input())

for _ in range(N):
    s=input()
    length=len(s)
    a=s[length//2]
    b=s[(length-1)//2]
    if a==b:
        print('Do-it')
    else :
        print('Do-it-Not')
