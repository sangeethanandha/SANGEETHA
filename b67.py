n=int(input("enter the number"))
digit=0
while n>0:
  digit=n%10
  if digit<=10:
    orgnum=10-digit
    orgnum1=orgnum+digit
    orgnum2=n-digit
    orgnum3=orgnum2+orgnum1
    print(orgnum3)
    break;
