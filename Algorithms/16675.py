ML, MR, TL, TR=input().split()

def play(A,B):
    res=''
    #print(A,B)
    if A==B:
        res='same'
    #A가 이기는 경우
    if (A=='S' and B=='P') or (A=='P' and B=='R') or (A=='R' and B=='S') :
        res='MS'
    #B가 이기는 경우
    if (A=='S' and B=='R') or (A=='P' and B=='S') or (A=='R' and B=='P'): 
        res='TK'
    return res
    

ans=[]

ans.append(play(ML,TL))
ans.append(play(ML,TR))
ans.append(play(MR,TL))
ans.append(play(MR,TR))


print(ans)

if ML==MR and (play(MR,TR)=='TK' or play(MR,TL)=='TK'):
    print('TK')
    exit()
if TL==TR and (play(MR,TR)=='MS' or play(ML,TR)=='MS'):
    print('MS')
    exit()

if ans.count('same')==2:
    print('?')
    exit()

if ('TK' in ans) and ('MS' in ans):
    print('?')
elif 'TK' in ans:
    print('TK')
elif 'MS' in ans :
    print('MS')
else:
    print('?')
