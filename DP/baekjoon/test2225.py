n,k = map(int,input().split());
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
  dp[i][1] = 1;
for i in range(2,k+1):
  for j in range(n+1):
    for a in range(j+1):
      dp[j][i] += dp[j-a][i-1];
print(dp[n][k]%1000000000);