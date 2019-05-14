n=int(input("enter the number"))
reverse=1
while(n<100000000000):
  reminder=n%10
  reverse=(reverse*1)*reminder
  n=n//10
print(reverse)
