import array
from array import *
limit=int(input("enter the limit"))
a=array('i',[])
for i in range(0,limit):
  m=int(input())
  a.append(m)
for i in a:
  ind=a.index(i)
  print(i,ind)
