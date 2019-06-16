cat,dog=map(int,input().split())
cat=cat^dog
dog=cat^dog
cat=cat^dog
print(cat,dog)
