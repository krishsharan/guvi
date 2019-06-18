x1,x2=map(int,input().split())
yy=list(map(int,input().split()))
count=0
if(len(yy)==x1):
 for i in yy:
  if(i==x2):
   count+=1
 print(count)  
