time1,minn1=[int(x) for x in input().split()]
time2,minn2=[int(y) for y in input().split()]
hour=time1-time2
minn=minn1-minn2
if hour<0:
  hours=-(hour)
  print(hours)
if minn<0:
  minn=-(minn)
  print(minn)
else:
  print(hour)
  print(minn)
