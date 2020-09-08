def rsp(x,y):
    if (x == 'R' and y == 'S') or (x == 'S' and y == 'P') or (x == 'P' and y == 'R'):
        return 'ms'
    elif (x == 'S' and y == 'R') or (x == 'P' and y == 'S') or (x == 'R' and y == 'P'):
        return 'tk'
    else:
        return 'none'

ml, mr, tl, tr = input().split()

result = set()
result.add(rsp(ml,tl))
result.add(rsp(ml,tr))
result.add(rsp(mr,tl))
result.add(rsp(mr,tr))

if (tl == tr) and (rsp(ml,tl)=='ms' or rsp(mr,tl)=='ms'):
    print('MS')
    exit()
if (ml == mr) and (rsp(ml,tl)=='tk' or rsp(ml,tr)=='tk'):
    print('TK')
    exit()

if 'ms' in result and 'tk' in result:
    print('?')
elif 'ms' in result:
    print('MS')
elif 'tk' in result:
    print('TK')
else:
    print('?')
