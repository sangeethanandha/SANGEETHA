a=int(input("enter the value for a"))
b=int(input("enter the value for b"))
if(a<=100000 and b<=100000):
  print("values before swapping a=",a,"b=",b)
  c=a
  a=b
  b=c
  print("values after swappinga=",a,"b=",b)
