n = int(input());
arr = list(map(int,input().split()));
# 순서를 뒤집어 가장 긴 증가하는 부분 수열 문제로 변환
arr.reverse();
DP = [1] * n;

#가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1,n):
  for j in range(0,i):
    if arr[j] < arr[i]:
      DP[i] = max(DP[i],DP[j]+1);
print(n - max(DP));