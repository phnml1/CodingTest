import sys
input = sys.stdin.readline;
n = int(input());
arr = []
for i in range(n):
  arr.append(input().rstrip());
sorted_arr = sorted(list(enumerate(arr)),key =  lambda x: x[1]);
def check(a,b):
  cnt = 0
  for i in range(min(len(a),len(b))):
    if a[i] == b[i]: cnt += 1;
    else: break
  return cnt;
length = [0] * (n+1)
maxlength = 0
for i in range(n-1):
  tmp = check(sorted_arr[i][1], sorted_arr[i+1][1]);
  maxlength = max(maxlength, tmp);
  
  length[sorted_arr[i][0]] = max(length[sorted_arr[i][0]],tmp);
  length[sorted_arr[i+1][0]] = max(length[sorted_arr[i+1][0]],tmp);

first = 0;
for i in range(n):
  if first == 0:
    if length[i] == max(length):
      first = arr[i]
      print(first)
      # 최장 접두사 저장
      pre = arr[i][:maxlength]
  else:
    if length[i] == max(length) and arr[i][:maxlength] == pre:
      print(arr[i]);
      break;