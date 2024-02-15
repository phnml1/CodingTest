t = int(input());
# eval로도

def dfs(sum, num, kind, n,string):
  if n == N:
    sum = sum + (kind * num)
    if sum ==0:
      print(string);
  else:
    dfs(sum,num*10+(n+1),kind,n+1,string+' '+str(n+1));
    dfs(sum+kind*num,n+1,1,n+1,string+'+'+str(n+1));
    dfs(sum+kind*num,n+1,-1,n+1,string+'-'+str(n+1));
for _ in range(t):
  N = int(input());
  dfs(0,1,1,1,'1');
  print();

# def recur(sum, sign, num, n, string):
#   if (n == N):
#     sum = sum + (sign*num)
#     if sum == 0:
#       print(string)
#   else:
#     recur(sum         ,sign , num*10+(n+1), n+1, string+' '+str(n+1))
#     recur(sum+sign*num,1    , (n+1)       , n+1, string+'+'+str(n+1))
#     recur(sum+sign*num,-1   , (n+1)       , n+1, string+'-'+str(n+1))
      
# test_case = int(input())

# for _ in range(test_case):
#   N = int(input())
#   recur(0,1,1,1,"1")
#   print()