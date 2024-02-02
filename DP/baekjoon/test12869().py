from itertools import permutations;
n = int(input());
scv = list(map(int,input().split()));
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)];
while len(scv) < 3:
  scv.append(0);

def mutal_attack(x,y,z,sum):
  global ans
  if x<=0 and y<=0 and z<=0:
    if ans>sum:
      ans = sum;
      return;
  x = 0 if x<=0 else x
  y = 0 if y<=0 else y
  z = 0 if z<=0 else z
  if dp[x][y][z]<=sum and dp[x][y][z]!=0:
    return
  dp[x][y][z] = sum;
  for a,b,c in permutations([9,3,1],3):
     mutal_attack(x-a,y-b,z-c,sum+1)
  return;
ans = float('inf')
mutal_attack(scv[0],scv[1],scv[2],0);
print(ans)