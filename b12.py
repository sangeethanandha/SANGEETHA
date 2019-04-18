N=int(input("enter the number"))
orgnum=N
rev=0
if(N<=1000):
  while(N>0):
    m=N%10
    rev=rev*10+m
    N=N//10
  if(orgnum==rev):
    print("YES")
  else:
    print("NO")
else:
  print("the given number is out of range")
