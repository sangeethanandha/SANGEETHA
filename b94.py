x,y=[int(x) for x in input().split()]
lst=[]
for i in range(1,X+1):
  n=int(input())
  lst.append(n)
print(lst)
for i in lst:
  if i==lst[y-1]:
    print(i)
