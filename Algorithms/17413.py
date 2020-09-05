S=input()

tag=''
ss=''

i=0
while i!=len(S):
    if S[i]=='<':
        print(ss[::-1],end='')
        ss=''
        while S[i]!='>':
            tag+=S[i]
            i+=1
        tag+=S[i]
        print(tag,end='')
        tag=''
        i+=1
        continue
    if i==len(S):
        break
    if S[i]==' ':
        print(ss[::-1],end=' ')
        ss=''
        i+=1
        continue
    
    ss+=S[i]
    i+=1


if len(ss)!=0:
    print(ss[::-1])
 
