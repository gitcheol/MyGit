N=int(input())
ans=[0]*1000001

for i in range(1,N+1):
    count=0
    tmp=list(str(i))
    length_of_tmp=len(tmp)
    for j in range(length_of_tmp):
        if tmp[j]=='3' or tmp[j]=='6' or tmp[j] =='9':
            count+=1 
    
    ans[i]=ans[i-1]+count 
 
print(ans[N])
