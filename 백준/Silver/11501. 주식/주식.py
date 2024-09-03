import sys;
input = sys.stdin.readline;

t = int(input());
for _ in range(t):
    n = int(input());
    stocks = list(map(int,input().split()));
    stocks.reverse();
    max_st = stocks[0];
    sum = 0;
    for i in range(1,n):
        if stocks[i] > max_st:
            max_st = stocks[i];
            continue;
        else:
            sum += max_st - stocks[i];
    print(sum);