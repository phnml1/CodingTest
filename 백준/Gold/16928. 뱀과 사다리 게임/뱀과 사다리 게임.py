from collections import defaultdict, deque
import sys
input = sys.stdin.readline;

n,m = map(int,input().split());
dict = defaultdict(int);
a = [1e9 for _ in range(101)];
for _ in range(n+m):
    x,y = map(int,input().split());
    dict[x] = y;
queue = deque();
a[1] = 0;
queue.append((0,1));
while queue:
    count, can = queue.popleft();
    if can == 100:
        break;
    for i in range(1,7):
        next_count = count + 1;
        next_can = can + i
        if 0<next_can <= 100:
            if next_can in dict:
                next_can = dict[next_can];
            if next_count < a[next_can]:
                a[next_can] = next_count;
                queue.append((next_count,next_can));
print(a[100]);
