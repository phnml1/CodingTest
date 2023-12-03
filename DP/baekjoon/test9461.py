import sys;
input = sys.stdin.readline;
n = int(input());
arr = []
for i in range(n):
  arr.append(int(input()));
result = []
for i in range(n):
  cur = arr[i]
  DP = [1 for _ in range(cur)];
  for i in range(3,cur):
    DP[i] = DP[i-3] + DP[i-2];
  result.append(DP[cur-1])
for res in result:
  print(res);