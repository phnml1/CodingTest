import sys
input = sys.stdin.readline;
n = int(input());
arr = list(map(int,input().split()));
arr.insert(0,0);

dp = [0] * (n+1);
for i in range(1,n+1):
  for k in range(1,n+1):
    if k-i>=0:
      dp[k] = max(arr[i] + dp[k-i], dp[k]);
print(dp[n]);