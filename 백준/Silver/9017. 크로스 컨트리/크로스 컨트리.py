from collections import defaultdict
import sys;
input = sys.stdin.readline;

t = int(input());
for _ in range(t):
  n = int(input());
  race = list(map(int,input().split()));
  teams = [];
  result = [];
  dic = defaultdict(list)
  min_result = 1e9;
  for r in race:
    if race.count(r) == 6:
      teams.append(r);
  for i in range(len(teams)):
    dic[teams[i]].append(i+1);
  for team in dic.keys():
    score = sum(dic[team][:4]);
    if min_result > score:
      min_result = score;
      result = [team];
    elif min_result == score:
      min_result = score;
      result.append(team);
  if len(result) == 1:
    print(result[0]);
  else:
    winners = [];
    for team in result:
      winners.append([dic[team][4],team]);
    winners.sort();
    print(winners[0][1]);