x=int(input())
if x>1:
  for i in range(2,x):
    if(x%i==0):
     print('yes')
     break
    elif x==1:
     print('no')
     break
else:
  print('no')
