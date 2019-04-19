N,Q=[int(x) for x in input().split()]
count=0
for i in range(N,Q+1):
  if i>1:
    for n in range(2,i):
      if((i%n)==0):
        break
    else:
      print(i,end=' ')
