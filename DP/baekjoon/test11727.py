n = int(input());
DP = [0 for _ in range(n+1)];
DP[1] = 1;
if n>=2:
  DP[2] = 3;
if n>=3:
  for i in range(3,n+1):
    DP[i] = DP[i-1] + DP[i-2]*2;
print(DP[n]%10007);