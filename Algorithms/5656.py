
ans=''
i=1
while True:
    S=input().split()
    if S[1]=='E':
        break
    S[0]=int(S[0])
    S[2]=int(S[2])
    # ">", ">=", "<", "<=", "==", "!="
    
    if S[1]=='>':
        if S[0] > S[2]:
           ans='true'
        else:
            ans='false'
    if S[1]=='>=':
        if S[0] >= S[2]:
           ans='true'
        else:
            ans='false'
    if S[1]=='<':
        if S[0] < S[2]:
           ans='true'
        else:
            ans='false'
    if S[1]=='<=':
        if S[0] <= S[2]:
           ans='true'
        else:
            ans='false'
    if S[1]=='==':
        if S[0] == S[2]:
           ans='true'
        else:
            ans='false'
    if S[1]=='!=':
        if S[0] != S[2]:
           ans='true'
        else:
            ans='false'

    print("Case "+str(i)+': '+ans)
    i+=1
