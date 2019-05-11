n,k=[int(x) for x in input().split()]
lst=[]
count=0
for i in range(0,n):
  m=int(input())
  lst.append(m)
for j in lst:
  if j==k:
    count=count+1
print(count)
