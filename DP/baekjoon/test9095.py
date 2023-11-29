import sys
input = sys.stdin.readline;
n = int(input());
arr =[]
for i in range(n):
  arr.append(int(input()));
for i in range(n):
  cur = arr[i];
  DP = [0 for _ in range(cur+1)];
  DP[0] = 1;
  for j in range(cur+1):
    for k in range(1,4):
      if j-k>=0:
        DP[j] += DP[j-k];
  print(DP[cur])