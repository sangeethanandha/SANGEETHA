x,y=[int(x) for x in input().split()]
for num in range(x,y):
  sum=0
  temp=num
  while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
  if num==sum:
    print(num)
