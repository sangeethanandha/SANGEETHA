N,Q=[int(x) for x in input().split()]
if(N<=100000) and (Q<=100000)):
  for i in range(N+1,Q):
    if(i%2!=0):
      print(i,end=' ')
  
    
