# from collections import Counter
# r,c,k = map(int,input().split());
# arr = [[0 for _ in range(3)] for _ in range(3)]
# for i in range(3):
#   newarr = list(map(int,input().split()));
#   for j in range(len(newarr)):
#     arr[i][j] = newarr[j];
# t = 0;
# while True:
#   matrix = []
#   if arr[r-1][c-1] == k:
#     print(t);
#     break;
#   if t>=100:
#     print(-1)
#     break;
#   if len(arr[0])>=len(arr):
#     matrix = list(zip(*arr));
#     for i in range(len(matrix)):
#       a = list(matrix[i]);
#       a.sort();
#       newarr= [];
#       cnt = Counter(a)
#       for key in cnt:
#         if key == 0:
#           continue;
#         newarr.append(key);
#         newarr.append(cnt[key]);
#       matrix[i] = newarr;
#     max_len = max(map(len,matrix));
#     for i in range(len(matrix)):
#       temp = list(matrix[i])
#       while len(temp)<max_len and len(temp)<3:
#         temp.append(0);
#       if len(temp)>100:
#         temp = temp[:100];
#       matrix[i] = temp;
#     arr = list(zip(*arr));
#     for i in range(len(arr)):
#       temp = list(arr[i])
#       while len(temp)<max_len and len(temp)<3:
#         temp.append(0);
#       if len(temp)>100:
#         temp = temp[:100];
#       arr[i] = temp;
#   else:
#     for i in range(len(arr)):
#       a = list(arr[i]);
#       a.sort();
#       newarr= [];
#       cnt = Counter(a)
#       for key in cnt:
#         if key == 0:
#           continue;
#         newarr.append(key);
#         newarr.append(cnt[key]);
#       arr[i] = newarr;
#     max_len = max(map(len,arr));
#     for i in range(len(arr)):
#       while len(arr[i])<max_len or len(arr[i])<3:
#         arr[i].append(0);
#       if len(arr[i])>100:
#         arr[i] = arr[i][:100];
  
#   t+=1;

r,c,k = map(int,input().split())

A = [ list(map(int,input().split())) for _ in range(3) ]

def calR():

    global A

    new_graph = [] 

    for i in A:

        elem = set(i) # 한 행의 원소만 추출
        temt = [] # (원소, 갯수) 를 담을 그래프
        temt2 = [] # 새로운 행이 될 그래프
        for j in elem:
            if j==0:
                continue
            cnt = i.count(j)
            temt.append((j,cnt))

        temt.sort(key=lambda x:(x[1],x[0]))

        for k in temt:
            temt2.append(k[0])
            temt2.append(k[1])

        temt2 = temt2[:100] # 100개 제한

        new_graph.append(temt2)


    max_len = max(map(len,new_graph))

	# 빈 칸은 0만큼 채워준다.
    for i in range(len(new_graph)):
        while len(new_graph[i]) !=max_len:
            new_graph[i].append(0)

    A = new_graph


for i in range(101):

    try:
        if A[r-1][c-1]==k:
            print(i)
            break
    except:
        pass

    if len(A[0]) > len(A):
        A = list(map(list,zip(*A)))
        calR()
        A = list(map(list,zip(*A)))
    else:
        calR()

else:
    print(-1)
