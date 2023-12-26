# p325 1,2
def solution(s):
    num = len(s)//2;
    answer = len(s)
    for step in range(1,num+1):
        # start = i;
        prev = s[0:step];
        count = 1;
        compressed = ''
        # while start< len(s):
        #     now = s[start:start+i];
        #     if prev ==now:
        #         count += 1;
        #     else:
        #         if count >= 2:
        #             compressed += str(count) + prev
        #         else:
        #             compressed += prev
        #         count = 1;
        #     prev = now
        #     start += i
        for j in range(step,len(s),step):
          # 이전 상태와 동일하다면 압축 횟수(count) 증가
          if prev == s[j:j+step]:
            count += 1
          # 다른 문자열이 나왔다면 (더 이상 압축하지 못하는 경우)
          else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j+step];
            count = 1;
        compressed += str(count) + prev if count>=2 else prev
        answer = min(answer,len(compressed));
    return answer