n=int(input())
a=n
b=0
while(n>0):
 m=n%10
 n=n//10
 c=m**3
 b=b+c
if(a==b):
 print('yes')
else:
 print('no')

 
