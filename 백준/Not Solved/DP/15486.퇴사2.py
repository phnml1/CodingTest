import sys;
input = sys.stdin.readline;

n = int(input());
arr = []
for _ in range(n):
  arr.append((list(map(int,input().split()))))
DP = [0 for _ in range(n+1)];
profit = 0;
for i in range(len(arr)):
  profit = max(profit,DP[i]);
  t,p = arr[i];
  if i + t<=n:
    DP[i+t] = max(profit + p,DP[i+t]);
print(max(DP));  