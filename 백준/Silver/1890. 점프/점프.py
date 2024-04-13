import sys;
input = sys.stdin.readline;

n = int(input());
arr = [];
for _ in range(n):
  arr.append(list(map(int,input().split())));
DP = [[0 for _ in range(n)] for _ in range(n)];
DP[0][0] = 1;
for i in range(n):
  for j in range(n):
    
    if i==n-1 and j==n-1:
      print(DP[i][j]);
    
    if j + arr[i][j] < n:
      DP[i][j+arr[i][j]] += DP[i][j];

    if i + arr[i][j] < n:
      DP[i+arr[i][j]][j] += DP[i][j];