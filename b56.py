str=input("enter the input")
count=0
sum=0
for i in str:
  if i.isdigit()==True:
    count=count+1
  elif i.isalpha()==True:
    sum=sum+1
  else:
    pass
if count==0 or sum==0:
  print("no")
else:
  print("yes")
