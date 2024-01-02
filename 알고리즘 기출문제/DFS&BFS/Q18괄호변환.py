#p.349
from collections import deque
a = input();
def isvalidate(st):
  queue = deque();
  for i in range(len(st)):
    if st[i] == '(':
        queue.append(st[i]);
    else:
      if queue:  
        queue.popleft();
  if queue:
    return False;
  return True;
def balanced_index(st):
  count = 0
  for i in range(len(st)):
    if st[i] == '(':
      count += 1;
    else:
      count -= 1
  if count ==0:
    return i;
  
def solution(p):
  answer = ''
  if p == '':
    return answer
  index = balanced_index(p);
  u = p[:index+1];
  v = p[index+1:];
  if isvalidate(u):
    answer = u+solution(v);
  else:
    answer = '(';
    answer += solution(v);
    answer += ')';
    u = list(u[1:-1]); # 첫 번째와 마지막 문자를 제거
    for i in range(len(u)):
      if u[i] == '(':
        u[i] = ')';
      else:
        u[i] = '(';
      answer += ''.join(u);
    return answer;
  
    