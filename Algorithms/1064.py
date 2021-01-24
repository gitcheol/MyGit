import math

Ax,Ay,Bx,By,Cx,Cy = map(int,input().split())

line1 = math.sqrt((Ax-Bx)**2 + (Ay-By)**2)
line2 = math.sqrt((Bx-Cx)**2 + (By-Cy)**2) 
line3 = math.sqrt((Ax-Cx)**2 + (Ay-Cy)**2) 

lines = []
lines.append(line1)
lines.append(line2)
lines.append(line3)
lines.sort()

if lines[0]+lines[1] == lines[2]:
    print(-1)
    exit()

ans = (lines[-1]-lines[0])*2
print(ans)
