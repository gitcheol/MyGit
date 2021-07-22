A,B=input().split()

def solve(a,b):
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    return count

min_val=10000
diff=len(B)-len(A)
for i in range(diff+1):
    s='0'*i+A+'0'*(diff-i) 
    tmp=solve(s,B)
    tmp-=diff
    if tmp < min_val:
        min_val=tmp

print(min_val)


