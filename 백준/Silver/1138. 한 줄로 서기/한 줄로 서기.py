#다시풀어라
import sys;
input = sys.stdin.readline;

n = int(input());
arr = list(map(int,input().split()));
location = [0] * n;
for i in range(n):
  count = 0;
  j = 0;
  while count < arr[i]:
    if location[j] == 0:
      count += 1;
    j += 1;
  while location[j] != 0:
    j+=1;
  location[j] = str(i+1);
      
result = ' '.join(location)
print(result);
