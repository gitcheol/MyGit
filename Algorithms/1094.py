x=int(input())
stick=[64]
ans=0
while True:
    if sum(stick)==x:
        print(len(stick))    
        break
    ans+=1
    stick=sorted(stick)
    cut=stick.pop(0)//2
    if sum(stick)+cut >= x:
        stick.append(cut)
    else : 
        stick.append(cut)
        stick.append(cut)
