N=int(input())

book={}

for i in range(N):
    name=input()
    if name in book:
        book[name]+=1
    else :
        book[name]=1 


best=max(book.values())

books=list(book.items())
ans=[]
for i in range(len(books)):
    if books[i][1]==best:
        ans.append(books[i][0])

ans.sort()
print(ans[0])
