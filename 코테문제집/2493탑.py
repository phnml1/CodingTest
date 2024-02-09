n = int(input())
heights = list(map(int,input().split()));
stack = [];
answers = [];
for i in range(n):
  while stack:
    # 송신 가능
    if stack[-1][1] >= heights[i]:
      answers.append(stack[-1][0]);
      break;
    #송신불가
    else:
      stack.pop();
  if not stack:
    answers.append(0);
  #차피 뒤에 있는애들중에서 제일높은애가 받음
  stack.append([i+1,heights[i]]);
for answer in answers:
  print(answer,end=' ');