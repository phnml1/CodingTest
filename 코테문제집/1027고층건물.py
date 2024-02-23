import sys
input = sys.stdin.readline;
n = int(input());
arr = list(map(int,input().split()));
result = 0

for i1, y1 in enumerate(arr):
  maxxy = sys.maxsize
  count = 0;
  if i1>0:
    for i in range(i1-1,-1,-1):
      if i == -1: break
      xy = (y1-arr[i])/(i1 - i);
      if maxxy > xy:
        count += 1;
        maxxy = xy;
  maxxy = -sys.maxsize;
  if i1<len(arr)-1:
    for i in range(i1+1,len(arr)):
      if i == n: break
      xy = (y1-arr[i])/(i1-i);
      if maxxy < xy:
        count+=1;
        maxxy = xy;
  if count > result: result = count;
print(result);