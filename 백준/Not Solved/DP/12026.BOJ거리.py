import sys; 
input = sys.stdin.readline;

n = int(input());
blocks = list(input().rstrip());
visited = True;
dp = [[1e9, not visited] for _ in range(n)];
dp[0][0], dp[0][1] = 0, True;

for i in range(1,n):
  block = blocks[i];
  check_jump = '?';
  
  if block == 'B':
    check_jump = 'J';
  elif block == 'O':
    check_jump = 'B';
  else:
    check_jump = 'O';
    
  for j in range(i):
    if check_jump == blocks[j]:
      dp[i][0] = min(dp[i][0],dp[j][0] + pow(i-j,2));
      
      if dp[i][0] != 1e9:
        dp[i][1] = True;
        
if dp[n-1][0] != 1e9:
  print(dp[n-1][0]);
else:
  print(-1); 