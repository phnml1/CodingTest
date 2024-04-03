import sys;
input = sys.stdin.readline;
strs = input().rstrip();
stack = []
result = 0;
tmp = 1;
brackets = [['(','['],[')',']']];
depth = [];

for i in range(len(strs)):
  str = strs[i];
  if str in brackets[0]:
    if str == brackets[0][0]:
      tmp *= 2
    if str == brackets[0][1]:
      tmp *= 3;
    stack.append(str);
  else:
    if len(stack) == 0:
      result = 0;
      break;
    if str == brackets[1][0]:
      if stack[-1] == brackets[0][0]:
        if strs[i-1] == '(':
          result += tmp
        tmp //= 2;
        stack.pop();       
      else:
        result = 0;
        break;
    if str == brackets[1][1]:
      if stack[-1] == brackets[0][1]:
        if strs[i-1] == '[':
          result += tmp;
        tmp //= 3;
        stack.pop();
      else:
        result = 0;
        break;

if len(stack)>0:
  print(0);
else:
  print(result);