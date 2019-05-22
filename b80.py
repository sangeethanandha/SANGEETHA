n=int(input("enter the number"))
lst=[]
while n>0:
  digit=n%10
  lst.append(digit)
  n=n//10
for i in lst:
  if i%2!=0:
    print(i,end=' ')
