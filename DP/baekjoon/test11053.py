import sys
input = sys.stdin.readline;
n = int(input());
arr = list(map(int,input().split()));
#DP는 인덱스를 가지는 arr 요소 값을 마지막값으로 가지는 수열
DP = [1 for _ in range(n)];
for i in range(1,n):
  for j in range(i):
    if arr[j] < arr[i]:
      DP[i] = max(DP[i],DP[j]+1)
      
print(max(DP));
    