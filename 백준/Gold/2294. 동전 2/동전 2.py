n,k = map(int,input().split());
coins = []
DP = [1e9 for _ in range(k+1)];
for _ in range(n):  
  coins.append(int(input()));
coins.sort();
DP[0] = 0;
for c in coins:
  for j in range(c,k+1):
    if DP[j] > 0:
      DP[j] = min(DP[j-c]+1, DP[j]);
if DP[k] == 1e9:
  print(-1);
else:
  print(DP[k]);
