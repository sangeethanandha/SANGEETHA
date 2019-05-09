n=int(input("enter the number"))
first=1
second=1
print(first)
print(second)
for i in range(1,n-1):
  temp=first+second
  first=second
  second=temp
  print(temp)
