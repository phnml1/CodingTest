import sys;
input = sys.stdin.readline;

s = input().rstrip();
t = input().rstrip();
def dfs(t,s):
  if t == s:
    print(1);
    sys.exit();
  if len(t) == len(s):
    return;
  if t[-1] == 'A':
    dfs(t[:-1],s);
  if t[0] == 'B':
    dfs(t[1:][::-1],s);

dfs(t,s);
print(0);