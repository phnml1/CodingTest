n = int(input());
arr = list(map(int,input().split()));

DP = [1] * n;
for i in range(1,n):
  for j in range(0,i):
    if arr[j] < arr[i]:
      DP[i] = max(DP[i],DP[j]+1);
print(n - max(DP));