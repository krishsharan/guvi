x=int(input())
y=list(map(int,input().split()))
for i in range (len(y)):
  if(y[i]>y[i+1]):
    break
print(i)
