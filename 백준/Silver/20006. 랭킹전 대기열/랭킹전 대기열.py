import sys;
input = sys.stdin.readline;
#dict는 순서보장 x
p,m = map(int,input().split());
players = [];
for _ in range(p):
  l,n = input().split();
  players.append([l,n]);
rooms = [];
for player in players:
  l,n = player;
  flag = False;
  for i in range(len(rooms)):
    level,_ = rooms[i][0];
    if int(level)-10<=int(l)<=int(level)+10 and len(rooms[i])<m:
      rooms[i].append([l,n]);
      flag = True;
      break;
  if flag == False:
    rooms.append([[l,n]]);
for room in rooms:
  if len(room)<m:
    print('Waiting!');
  else:
    print('Started!');
  room.sort(key=lambda x: x[1]);
  for player in room:
    print(*player);
