x=str(input())
y=len(x)
mid=int((y-1)/2)
if y%2!=0:
 print(x[0:mid]+'*'+x[mid+1:])
else:
    print(x[0:mid]+'**'+x[mid+2:])
