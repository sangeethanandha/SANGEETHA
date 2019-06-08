n=int(input("enter the limit"))
l=[]
for i in range(n):
    num=int(input("enter the num"))
    l.append(num)
for j in l:
    l.sort(reverse=False)
print(l)
