import sys;
input = sys.stdin.readline;

n = int(input());
tops = list(map(int,input().split()));
max_h = 0;
stack = [[1,tops[0]]];
result = [0 for _ in range(n)];
for i in range(1,len(tops)):
  while stack and stack[-1][1]<=tops[i]:
    stack.pop();
  if stack:
    result[i] = stack[-1][0];
  stack.append([i+1,tops[i]]);
for res in result:
  print(res, end = ' ');
  