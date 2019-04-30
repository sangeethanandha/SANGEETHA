s=int(input("enter the number"))
x,y=[int(x) for x in input().split()]
if((x<s) and (s<y)):
  print("yes")
else:
  print("no")
