from collections import defaultdict
import sys;

input = sys.stdin.readline;

n,k = map(int,input().split());
sequence = list(map(int,input().split()));
dic = defaultdict(int);
left,right = 0,0;
result = 0;

while right < len(sequence):
  if dic[sequence[right]] >= k:
    dic[sequence[left]] -= 1; 
    left+=1; 
  else:
    dic[sequence[right]] += 1;
    right += 1;
    result = max(result,right - left);
      
print(result);