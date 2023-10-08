#내풀이
# mapx,mapy = map(int,input().split());
# myx,myy,mydir = map(int, input().split());
# gamemap = []

# for j in range(mapx):
#         values = list(map(int, input().split()));
#         gamemap.append(values);
# dirs = [(-1,0),(0,1),(1,0),(-1,0)];
# result = 0

# while True:
#     if(gamemap[myx][myy]==1):
#         break;
#     gamemap[myx][myy] = 2;
#     result += 1;
#     dirnum = mydir
#     count = 0
#     for _ in range(4):    
#         if dirnum==0:
#             dirnum = 3;
#         else:
#             dirnum = dirnum - 1;
#         dx,dy = dirs[dirnum];
#         if(gamemap[myx+dx][myy+dy]==1 or gamemap[myx+dx][myy+dy]==2 or myx+dx<0 or myx+dx>=mapx or myy+dy<0 or myy+dy>=mapy):
#             count+=1;
#             continue;
#         else:
#             myx,myy = myx+dx,myy+dy;
#             count=0;
#             break;
#     if count==4:
#         dx,dy = dirs[dirnum];
#         if(gamemap[myx-dx][myy-dy]==1 or myx-dx<0 or myx-dx>=mapx or myy-dy<0 or myy-dy>=mapy):
#             print(result);
#             break;
    
#책풀이
n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x,y,direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction=3
count =1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        count += 1
        turn_time = 0
        continue
    else:
        turn_time+=1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(count)
        
    