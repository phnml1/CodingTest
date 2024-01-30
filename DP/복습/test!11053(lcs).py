n = int(input());
arr = list(map(int,input().split()));
DP = [1 for _ in range(n)];
for i in range(n):
  for j in range(i):
    if arr[j] < arr[i]:
      DP[i] = max(DP[j]+1,DP[i]);
print(max(DP));