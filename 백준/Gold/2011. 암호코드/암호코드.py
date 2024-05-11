import sys
input = sys.stdin.readline;
a = input().rstrip();
dp = [0 for _ in range(len(a)+1)];
dp[0] = 1;
if a[0] =='0':
  print(0);
  sys.exit();
for i in range(1,len(a)+1):
  count = 0;
  if int(a[i-1]) > 0:
    count += dp[i-1];
  if i-2>=0:
    if 10<=int(a[i-2:i])<=26:
      count += dp[i-2];
  dp[i] = count%1000000;
print(dp[-1]);