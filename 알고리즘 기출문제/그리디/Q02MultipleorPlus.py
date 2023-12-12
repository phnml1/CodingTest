# 314쪽
a = input();
result = int(a[0]);
for i in range(1,len(a)):
  curnum = int(a[i]);
  if result<=1 or curnum<=1:
    result += curnum;
  else:
    result *= curnum;
print(result)