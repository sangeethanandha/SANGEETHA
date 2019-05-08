str=input("enter the string")
vowels="aeiou"
count=0
for i in str:
  if i in vowel:
    count=count+1
if(count>0):
  print("yes")
else:
  print("no")
