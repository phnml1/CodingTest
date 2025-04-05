import sys
from itertools import combinations
input = sys.stdin.readline;

n,m = map(int,input().split());
arr = list(map(int,input().split()));
arr.sort();
cases = combinations(arr,m)

for case in cases:
  for num in case:
    print(num, end = ' ');
  print();