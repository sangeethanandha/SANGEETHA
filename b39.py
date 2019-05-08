limit=int(input("enter the limit"))
lst=[]
for i in range(0,limit):
  m=input()
  lst.append(m)
big=lst[0]
for j in lst:
  if j>big:
    big=j
print(j)
