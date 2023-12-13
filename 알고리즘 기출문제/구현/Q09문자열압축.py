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
          if prev == s[j:j+step]:
            count += 1
          else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j+step];
            count = 1;
        compressed += str(count) + prev if count>=2 else prev
        answer = min(answer,len(compressed));
    return answer