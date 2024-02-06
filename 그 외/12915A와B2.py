# 시간 초과
# import sys
# input = sys.stdin.readline;
# s = input().rstrip();
# t = input().rstrip();
# result = 0;
# def game(st):
#   global result;
#   if len(st)==len(t):
#     if st == t:
#       print(1);
#       return;
#     else:
#       return;
#   new_s = st + 'A';
#   game(new_s)    
#   new_s = (st + 'B')[::-1];
#   game(new_s);
# game(s)
# print(result);

# T를 S로 바꾸는것 거꾸로!
import sys
input = sys.stdin.readline;
s = input().rstrip();
t = input().rstrip();
def game(t):
  if t ==s:
    print(1);
    sys.exit();
  if len(t) == 0:
    return 0;
  if t[-1] == 'A':
    game(t[:-1]);
  if t[0] == 'B':
    game(t[1:][::-1]);
game(t);
print(0);
  