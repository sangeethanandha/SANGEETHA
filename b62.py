n=int(input("enter the number"))
lst=[]
count=0
while(n>0):
    digit=n%10
    lst.append(digit)
    n=n//10
for i in lst:
    if i==0 or i==1:
        pass
    else:
        count=count+1
if count<=0:
    print("Yes")
else:
    print("No")
