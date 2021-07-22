N=int(input())
switch=list(map(int,input().split()))
switch.insert(0,3)
stu_num=int(input())

for i in range(stu_num):
    sex,num=map(int,input().split())
    
    if sex==1:
        tmp=1
        while num*tmp<=N:
           if switch[num*tmp]==1:
               switch[num*tmp]=0
           else :
               switch[num*tmp]=1
           tmp+=1
    else :
        tmp=0
        while num-tmp>0 and num+tmp<=N:
            if switch[num+tmp]==switch[num-tmp]:
                tmp+=1
            else :
                break

        tmp-=1
        for j in range(num-tmp,num+tmp+1):
            if switch[j]==1:
                switch[j]=0
            else:
                switch[j]=1

for i in range(1,N+1):
    print(switch[i],end=' ')
    if i%20==0:
        print()

