import sys;
input = sys.stdin.readline;

s = input().rstrip();
index = [[],[]];
result_index = [];
result = '';
for i in range(len(s)):
  index[int(s[i])].append(i);
result_index = index[0][:len(index[0])//2] + index[1][len(index[1])//2:]
for i in result_index:
  result += s[i];
print(result); 