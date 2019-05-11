str=input("enter your string")
n=int(input("enter the number"))
count=0
for i in str:
  count=count+1
  if count<=n:
    print(i,end='')
