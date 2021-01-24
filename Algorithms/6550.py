while True:
    try:
        s, t = input().split()
        flag = False
        idx = 0
        for i in t : 
            if s[idx] == i : 
                idx+=1
                if idx == len(s):
                    flag = True
                    break

        if flag:
            print('Yes')
        else : 
            print('No')
    except:
        break

