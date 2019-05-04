limit=int(input("enter the limit"))
lst=[]
sum=0
for i in range(0,limit):
  m=input()
  lst.append(m)
for j in lst:
  sum=sum+int(j)
avg=sum/limit
print(round(avg))
