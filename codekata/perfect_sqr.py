a,b=map(int,input().split())
c=a*b
for i in range (0,c+1):
 if(i**2==0):
   print('yes')
   break
else:
 print('no')
