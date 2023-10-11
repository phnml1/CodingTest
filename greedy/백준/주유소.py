n = int(input())
path = list(map(int, input().split()))
nodes = list(map(int, input().split()))
result = 0
cheap = nodes[0];
result+=path[0]*cheap;
for i in range(1,len(nodes)-1):
    if nodes[i]<cheap:
        cheap = nodes[i];
    result += cheap*path[i]

print(result)

        