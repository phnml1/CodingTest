import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000);
N = int(input());
sosu = [2,3,5,7];
result = []
def is_prime(num):
  for i in range(2,int(num/2)+1):
    if num%i == 0:
      return False;
  return True;
def dfs(num,n):
  if is_prime(num)==False:
    return;
  if n==N:
    result.append(num);
    return;
  for i in range(1,10):
    dfs(int(str(num) + str(i)), n+1);
for i in sosu:
  dfs(i,1);
result.sort();
for number in result:
  print(number);