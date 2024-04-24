import sys
input = sys.stdin.readline;

n = int(input());
arr = list(map(int,input().split()));
dp = [1 for i in range(n)];
for i in range(n):
  for j in range(i):
    if arr[j]<arr[i]:
      dp[i] = max(dp[i],dp[j]+1);
print(max(dp));
order = max(dp);
result = [];
for i in range(n-1,-1,-1):
  if dp[i] == order:
    result.append(arr[i]);
    order -= 1;
result.reverse();
print(*result);