#incluce<stdio.h>
#include<conio.h>
void main()
{
int n,temp,i,j,a[10];
float f;
clrscr();
scanf("%d",&n);
for(i=1;i<=n;i++)
{
scanf("%d",&a[i]);
}
for(i=1;i<=n;++)
{
for(j=i+1;j<=n;j++)
{
if(a[i]>a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
if(i%2==0)
{
printf("%d",a[i/2]);
}
else
{
f=i/2;
printf("%d",a[f]);
}
getch();
}
