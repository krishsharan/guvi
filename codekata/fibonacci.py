number=int(input())
A=0
B=1
while(number>0):
 print(B,end=' ')
 A,B=B,A+B
 number-=1
