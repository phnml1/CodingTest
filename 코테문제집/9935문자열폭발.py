import sys
input = sys.stdin.readline;
st = input().rstrip();
bomb = input().rstrip();
stack = []
result = ''
if st[0] == bomb[0]:
  stack.append([1,st[0]]);
else:
  stack.append([0,st[0]]);
#시간초과
for i in range(1,len(st)):
  if len(stack)>0:
    count,stack_st = stack[-1][0],stack[-1][1];
    if st[i] == bomb[count]:
      stack.append([count+1,st[i]]);
      if count == len(bomb)-1:
        sl = len(stack)-len(bomb)
        stack = stack[:sl];
    elif st[i] == bomb[0]:
      stack.append([1,st[i]]);
    else:
      stack.append([0,st[i]]);
  else:
    if st[i] == bomb[0]:
      stack.append([1,st[i]]);
    else:
      stack.append([0,st[i]])
if len(stack)>0:
  for i in range(len(stack)):
    result += stack[i][1];
else:
  result = 'FRULA';
print(result)