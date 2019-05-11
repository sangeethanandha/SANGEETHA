n=int(input("enter the number"))
lst=[]
for i in range(1,11):
  lst.append(i)
if n in lst:
  print("yes")
else:
  print("no")
