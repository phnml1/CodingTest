import copy;
import sys;
input = sys.stdin.readline
n = int(input());
arr = list(map(int,input().split()));
operator = list(map(int,input().split()));
max_result,min_result = -sys.maxsize,sys.maxsize

def calculate(index,cur_oper,oper,res):
  global max_result,min_result;
  if cur_oper == 0:
    res += arr[index];
  if cur_oper == 1:
    res -= arr[index];
  if cur_oper == 2:
    res *= arr[index];
  if cur_oper == 3:
    if res <0 and arr[index]>0:
      res =abs(res)//abs(arr[index]);
      res = -res;
    else:
      res = res//arr[index];
  for i in range(len(oper)):
    temp_oper = copy.deepcopy(oper);
    if oper[i] != 0:
      temp_oper[i] -= 1;
      calculate(index+1,i,temp_oper,res);
  if index == n-1:
    max_result = max(max_result,res);
    min_result = min(min_result,res);
    return;
calculate(0,0,operator,0)
print(int(max_result));
print(int(min_result));   
      
