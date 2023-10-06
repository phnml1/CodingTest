#나는 2차원배열을 

#책에서의 2중반복문풀이
n,m = map(int, input().split());

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result, min_value)
print(result)
#책에서의 min함수 풀이
# n,m = map(int, input().split);
# result = 0
# for i in range(n):
#     #리스트로 입력값받기 (외우기)
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)