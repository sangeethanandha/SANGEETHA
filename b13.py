n=int(input("enter the number"))
count=0
if(n<=1000):
  for i in range(1,n+1):
    if(n%i==0):
      count=count+1
  if(count==2):
    print("YES")
  else:
    print("NO")
