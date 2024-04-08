import sys
input=sys.stdin.readline
n = int(input());
arr = []

for _ in range(n):
  arr.append(list(input().rstrip()));
def count_max(arr):
  result = 1;
  for i in range(n):
    count = 1;
    for j in range(n-1):
      if arr[i][j] == arr[i][j+1]:
        count += 1;
      else:
        count = 1;
      result = max(result,count);
    count = 1;
    for j in range(n-1):
      if arr[j][i] == arr[j+1][i]:
        count += 1;
      else:
        count = 1;
      result = max(result,count);
  return result;
res = 1;
for i in range(n):
  for j in range(n):
    if j+1<n:
      arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j];
      res = max(res,count_max(arr));
      arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j];
    if i+1<n:
      arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j];
      res = max(res,count_max(arr));
      arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j];
print(res);