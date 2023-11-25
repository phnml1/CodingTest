# 2^n
# def fibo(n):
#   if n==1 or n==2:
#     return 1
#   return fibo(n-1)+fibo(n-2);

d =  [0]*100;
# n
def fibo(n):
  if n==1 or n==2:
    return 1;
  if d[n] !=0:
    return d[n]
  d[n] = fibo(n-1) +  fibo(n-2);
  return d[n];

d = [0] *100;
d[1] = 1;
d[2] = 2;
def fibo_iter(n):
  for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2];

  print(d[n]);