board=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

for row in board :
            for column in range(0,len(row)):
                num=0
                if column[x+1]==1 and column[x+1]<len(row):
                    num+=1
                if column[x-1]==1 and column[x-1]>=0:
                    num+=1
