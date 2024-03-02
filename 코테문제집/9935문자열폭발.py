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
if stack:
  print(*(list(zip(*stack))[1]),sep='')
else:
  print('FRULA')
  

# import sys
# x = list(sys.stdin.readline().strip())
# M = list(sys.stdin.readline().strip())
# m = len(M)
# stack = []
# for i in x:
#     stack.append(i)
#     if stack[len(stack)-m:len(stack)] == M: #스택의 끝부터 M의 글자열 크기까지 자른게 M과 같다면
#         for _ in range(m): # m의 길이만큼
#             stack.pop() # stack에서 꺼내준다!
# if stack:
#     print(*stack, sep='')
# else:
#     print("FRULA")