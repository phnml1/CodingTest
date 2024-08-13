import sys;
input = sys.stdin.readline;

n = int(input().strip());
str = input().strip();
result = 1e9;
rexplore = str.rstrip('R');
result = min(result, rexplore.count('R'));
rexplore = str.rstrip('B');
result = min(result, rexplore.count('B'));
rexplore = str.lstrip('R');
result = min(result, rexplore.count('R'));
rexplore = str.lstrip('B');
result = min(result, rexplore.count('B'));

print(result);
