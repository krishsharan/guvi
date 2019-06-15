y,z=map(int,input().split())
for i in range(y+1,z):
 sum=0
 temp=i
 while(temp>0):
  digit=temp%10
  sum+=digit**3
  temp=temp//10
 if(i==sum):
  print(i,end=" ")
