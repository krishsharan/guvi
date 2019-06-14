
p,q=map(int,input().split())
for x in range(p+1,q):
  if(x>1):
    for n in range(2,x):
      if(x%n)==0:
        break
    else:
      print(x,end=" ")
