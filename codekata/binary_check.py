x1=int(input())
x1=str(x1)
f=0
for i in range(0,len(x1)):
 if(x1[i]=='0' or x1[i]=='1'):
  f=1
 else:
  f=0
  break
if(f==1):
 print('yes')
else:
 print('no')
