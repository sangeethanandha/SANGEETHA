import array
from array import *
limit=int(input("enter the limit"))
if(limit<10000):
  print("enter the numbers in array:")
  lst=[]
  for i in range(int(limit)):
    n=input("number:")
    lst.append(int(n))
  print("ARRAY:",lst)
  min=lst[0]
  for i in lst:
    if(min>i):
      min=i
  print(min)
  max=lst[0]
  for i in lst:
    if(max<i):
      max=i
  print(max)
