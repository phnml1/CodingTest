import sys;
input = sys.stdin.readline
str1 = input().rstrip();
str2 = input().rstrip();
DP = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)];

for i in range(len(str1)):
  for j in range(len(str2)):
    if str1[i] == str2[j]:
      DP[i][j] = DP[i-1][j-1] + 1;
    else:
      DP[i][j] = max(DP[i][j-1],DP[i-1][j]);
print(DP[len(str1)-1][len(str2)-1]);