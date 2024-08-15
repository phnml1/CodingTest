import sys;
input = sys.stdin.readline;

n = int(input().strip());
a = list(map(int,input().split()));
location = [0 for _ in range(n)];

for i in range(len(a)):
  cnt = 0;
  for j in range(len(a)):
    if location[j] == 0 and cnt == a[i]:
      location[j] = i+1;
      break;
    elif location[j] == 0:
      cnt += 1;
      
print(' '.join(map(str, location)))