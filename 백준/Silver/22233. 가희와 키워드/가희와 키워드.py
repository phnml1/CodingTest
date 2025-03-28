import sys
from collections import defaultdict;
input = sys.stdin.readline;
n,m = map(int,input().split());
dict = defaultdict();

for _ in range(n):
    st = input().rstrip();
    if st in dict:
        dict[st] += 1;
    else:
        dict[st] = 1;
for _ in range(m):
    keywords = input().rstrip().split(',');
    for keyword in keywords:
        if keyword in dict:
            dict[keyword] -= 1;
            if dict[keyword] == 0:
                del dict[keyword];
    print(len(dict.keys()));