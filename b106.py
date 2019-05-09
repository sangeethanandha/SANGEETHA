n=int(input("enter the number"))
k=int(input("enter the number"))
lst=[]
count=0
for i in range(0,n):
  m=int(input())
  lst.append(m)
for j in lst:
  if j%2!=0:
    count=count+1
    if count==k:
      print(j)
