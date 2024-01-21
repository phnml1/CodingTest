# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

# 1+1+1+1
# 2+1+1 (1+1+2, 1+2+1)
# 2+2
# 1+3 (3+1)
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

from sys import stdin
input = stdin.readline;
t = int(input());
tc = []
dp = [[1 for _ in range(10001)] for _ in range(4)];
for i in range(2,4):
  for j in range(1,10001):
    if j>=i: 
      dp[i][j] = dp[i][j-i] + dp[i-1][j];
    else:
      dp[i][j] = dp[i-1][j];
for _ in range(t):
  tc.append(int(input()));
for a in tc:
  print(dp[3][a]);