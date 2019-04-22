n=int(input("enter the number"))
count=0
if(n<=100000):
  for i in range(1,n+1):
    count=count+i
  print(count)
