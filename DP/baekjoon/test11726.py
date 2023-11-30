import sys
input = sys.stdin.readline;

n = int(input());
DP = [0 for _ in range(n+1)];
DP[0] = 1;
for i in range(1,n+1):
  for j in range(1,3):
    if i-j>=0:
      if i==2:
        DP[i] += DP[i-j]*2-1;
      else:
        DP[i] += DP[i-j];
print(DP[n]%10007); 