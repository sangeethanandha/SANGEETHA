str=input("enter the string")
s=len(str)
lst=[]
strr=""
for i in str:
  lst.append(i)
if s%2==0:
  n=s//2
  lst[n]="*"
  lst[n-1]="*"
  for i in lst:
    strr=strr+i
  print(strr)
else:
  n=s//2
  lst[n]="*"
  for i in lst:
    strr=strr+i
  print(strr)
