# def solution(gems):
#     N = len(gems)
#     answer = [0, N-1]
#     kind = set(gems)
#     s,e = 0,0  # 투포인터
#     while 0<=s<N and 0<=e<N:
#         if set(gems[s:e+1]) == kind:  
#             if (e-s+1) < (answer[1]-answer[0]+1):
#                 answer = [s,e]
#             s += 1
#         else: 
#             e += 1
#     answer[0] += 1
#     answer[1] += 1
#     return answer

def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))  # 보석종류
    dic = {gems[0]:1,}  # 종류 체크할 딕셔너리
    s,e = 0,0  # 투포인터
    while s<N and e<N:
        if len(dic) < kind:  # 종류 부족하면 end point 증가 & dic 개수 증가
            e += 1
            if e == N:
                break
            # dic.get은 해당 키가 존재하면 그 키에 해당하는 값 반환 그렇지 않으면 0 반환
            dic[gems[e]] = dic.get(gems[e], 0) + 1
            
        else:  # 종류 같으면 ans 비교 후 답 갱신하고, start point 증가 & dic 개수 다운
            if (e-s+1) < (answer[1]-answer[0]+1):
                answer = [s,e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1
    answer[0] += 1
    answer[1] += 1
    return answer