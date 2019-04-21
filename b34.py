str=input("enter the lines")
count=1
for i in str:
  if(i=='.'):
    count=count+1
  else:
    continue
print(count)
