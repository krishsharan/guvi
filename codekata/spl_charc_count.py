word=input()
itr=0
for i in range (len(word)):
 if(word[i].isdigit() or word[i].isalpha() or word[i]==' '):
  continue
 else:
  itr+=1
print(itr)  
