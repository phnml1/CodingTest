n,m,l,k = map(int,input().split());
arr = []
for _ in range(k):
  x,y = map(int,input().split());
  arr.append((x,y))
result = 0
for sx,_ in arr:
  for _,ey in arr:
    count = 0;
    for ax,ay in arr:
      if sx<=ax<=sx+l and ey<=ay<=ey+l:
        count += 1;
    result = max(count,result);
print(k-result);