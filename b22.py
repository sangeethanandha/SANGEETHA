import array
from array import *
limit=int(input("enter the limit"))
if(limit<100000):
  print("enter the number in array:")
  lst=[]
  for i in range(int(limit)):
    n=input("number:")
    lst.append(int(n))
    print('ARRAY:',lst)
    max=lst[0]
    for i in lst:
      if(max<i):
        max=i
      print(max)
 
