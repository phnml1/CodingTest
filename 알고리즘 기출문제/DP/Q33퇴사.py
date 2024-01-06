n = int(input());
arr = []
for i in range(n):
  t,p = map(int,input().split());
  arr.append((t,p));
DP = [0 for _ in range(n+1)];
for i in range(n):
  t,p = arr[i];
  if i!=0:
    DP[i] = max(DP[i-1],DP[i]);
  if i+t <= n:  
    DP[i+t] = max(DP[i+t], p + DP[i]);
if DP[n] == 0:
  DP[n] = DP[n-1];
print(DP[n])
