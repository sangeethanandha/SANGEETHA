n=int(input("enter the number"))
count=0
for i in range(1,n+1):
  if n%1==0:
    count=count+1
if count==2:
  print("no")
else:
  print("yes")
