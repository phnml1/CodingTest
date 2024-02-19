import sys
input = sys.stdin.readline
n = int(input());
result = 0;
arr = list(map(int,input().split()));
arr.sort();
for i in range(n):
  tmp = arr[:i] + arr[i+1:];
  left,right = 0, len(tmp)-1;
  while left<right:
    sum = tmp[left] + tmp[right];
    if sum < arr[i]:
      left = left + 1;
    elif sum>arr[i]:
      right = right -1;
    else:
      result += 1;
      break;
print(result);
  