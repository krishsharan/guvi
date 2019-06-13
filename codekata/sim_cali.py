a=input("Give 1st input")
print(" The operations are 1.Addition 2.Subtraction 3.Multiplication 4.Division 5. Quit")
t=1
ans=0
while (1):
  if(t!=1):
    a=ans
  choice=int(input("OP: "))
  b=input("Give 2nd input: ")
  if choice==1:
    ans = float(a) + float(b)
  if choice==2:
    ans = float(a) - float(b)
  if choice==3:
    ans = float(a) * float(b)
  if choice==4:
    ans = float(a) / float(b)
  print(ans)
  if(choice==5):
    break
  t+=1
