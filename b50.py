n=int(input("enter the number"))
if n%2!=0 or n==1 or n==0:
  print("no")
else:
  while(n%2!=1):
    n=n//2
    print("yes")
