n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int,input().split())));
for i in range(1,n):
  m = len(arr[i]);
  for j in range(m):
    if j-1>=0 and j<m-1:
      arr[i][j] = arr[i][j] + max(arr[i-1][j-1],arr[i-1][j]);
    if j==0:
      arr[i][j] = arr[i][j] + arr[i-1][j]
    if j==m-1:
      arr[i][j] = arr[i][j] + arr[i-1][j-1];
print(max(arr[n-1]));