c,n = map(int,input().split());
arr = []
for _ in range(n):
  arr.append(map(int,input().split()));
DP = [1e9 for _ in range(c+100)];
DP[0] = 0
for i in range(n):
  w,v = arr[i];
  for j in range(v,c+100):
    DP[j] = min(DP[j-v] + w, DP[j])
print(min(DP[c:]));