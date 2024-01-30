n = int(input());
for _ in range(n):
  t = int(input());
  arr = list(map(int,input().split()));
  dp = [[0 for _ in range(t+1)] for _ in range(t+1)]
  for i in range(t-1):
    dp[i][i+1] = arr[i] + arr[i+1];
  for i in range(t-2,-1,-1):
    for j in range(1,t):
      if dp[i][j] == 0 and i<j:
        # dp[i][k] + dp[k+1][j]의 값은 한 페이지를 만들 때의 최솟값이 아닌 두 페이지를 만들 때의 최솟값이다. 그리고 두 페이지를 합칠 때의 비용은 i에서 j까지의 모든 비용의 합을 더한 값이다.
        dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(arr[i:j+1]);
  print(dp[0][t-1])