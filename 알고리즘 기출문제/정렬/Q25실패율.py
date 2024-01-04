# 내 코드
# def solution(N, stages):
#     stages.sort();
#     results = []
#     answer = []
#     stageNumbers = []
#     prev = stages[0];
#     denomin = len(stages);
#     mole = 1;
#     for i in range(N):
#         stageNumbers.append(i+1);
#     for i in range(1,len(stages)):
#         if stages[i] == prev:
#             mole += 1;
#         if stages[i] != prev or i==len(stages)-1:
#             results.append([prev,mole/denomin]);
#             denomin -= mole
#             mole = 1;
#             prev = stages[i];
#         if stages[i]>N:
#             break;
#     results.sort(reverse=True,key = lambda x: (x[1],-x[0]))
#     for result in results:
#         answer.append(result[0])
#     stageNumbers = list(set(stageNumbers) - set(answer));
#     stageNumbers.sort();
#     answer = answer + stageNumbers
#     return answer
# print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]));

def solution(N, stages):
    answer = []
    length = len(stages);
    
    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1,N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0;
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i,fail));
        length -= count
    
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key = lambda t: t[1], reverse=True);

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer];
    return answer