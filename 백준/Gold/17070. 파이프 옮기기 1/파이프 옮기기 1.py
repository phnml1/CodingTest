import sys;
input = sys.stdin.readline;
n = int(input());
arr = []
result = 0;
for _ in range(n):
  arr.append(list(map(int,input().split())));
dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(3)];
dp[0][0][1] = 1;

for i in range(2,n):
  if arr[0][i] == 0:
    dp[0][0][i] = dp[0][0][i-1];
for r in range(1,n):
  for c in range(1,n):
    if arr[r][c] == 0 and arr[r-1][c] == 0 and arr[r][c-1] == 0:
      dp[2][r][c] = sum(dp[i][r-1][c-1] for i in range(3));
    if arr[r][c] == 0:
      dp[0][r][c] = dp[2][r][c-1] + dp[0][r][c-1];
      dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c];
print(sum(dp[i][n-1][n-1] for i in range(3)));