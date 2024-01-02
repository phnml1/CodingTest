# p351
n = int(input());
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split());
min_value = 1e9;
max_value = 0;
def solution(i,now):
  #이렇게할시 글로벌변수 쓸수있음
  global min_value,max_value,add,sub,mul,div;
  if i == n:
    min_value = min(min_value, now);
    max_value = max(max_value, now);
  else:
    if add>0:
      add -= 1;
      solution(i+1,now+data[i]);
      add += 1;
    if sub > 0:
      sub -= 1;
      solution(i+1, now-data[i]);
      sub +=1;
    if mul > 0:
      mul -= 1;
      solution(i+1, now*data[i]);
      mul +=1;
    if div > 0:
      div -= 1;
      #//쓸시 음수에서는 내림적용
      solution(i+1, int(now/data[i]));
      div += 1;             
        
solution(1,data[0]);
print(max_value);
print(min_value)
