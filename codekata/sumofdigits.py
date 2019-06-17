inp=int(input())
sum=0
while(inp>0):
 digit=inp%10
 inp=inp//10
 sum+=digit
print(sum) 
