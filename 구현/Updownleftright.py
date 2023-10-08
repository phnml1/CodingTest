# num = input()
# #ways = list(map(str, input().split()));
# ways = input.split()
# x,y = 1,1
# for way in ways:
#     if(way == 'R'):
#         if(x<5):
#             x += 1;
#     elif(way=='U'):
#         if(y>1):
#             y-=1;
#     elif(way=='D'):
#         if(y<5):
#             y+=1
#     elif(way=='L'):
#         if(x>1):
#             x-=1
#     else:
#         print('잘못된 입력값입니다.')
# print(y,x)

n = int(input())
x,y = 1,1
plans = input().split();

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == more_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx>n or ny>n:
        continue
    x,y = nx,ny
print(x,y)

