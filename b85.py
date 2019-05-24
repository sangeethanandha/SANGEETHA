str=input("enter the string")
lst=list(str)
even=""
odd=""
i=1
for j in lst:
  if i%2==0:
    even=even+j
  else:
    odd=odd+j
  i=i+1
print(odd, even)
