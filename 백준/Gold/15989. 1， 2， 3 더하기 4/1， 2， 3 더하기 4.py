#다시풀어라
import sys;
input = sys.stdin.readline;

dp = [[0 for _ in range(10001)] for _ in range(4)];
dp[1][0],dp[2][0],dp[3][0] = 1,1,1;

for i in range(1,10001):
  dp[1][i] = 1;
for i in range(2,4):
  for j in range(1,10001):
    if j - i>=0:
      dp[i][j] = dp[i][j-i] + dp[i-1][j];
    else:
      dp[i][j] = dp[i-1][j];
t = int(input());
for _ in range(t):
  print(dp[3][int(input())]);


