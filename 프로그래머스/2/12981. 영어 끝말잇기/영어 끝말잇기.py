def solution(n, words):
    answer = []
    prev_word = words[0][-1];
    prev_words = {};
    prev_words[words[0]] = 0;
    for i in range(1,len(words)):
        word = words[i];
        if prev_word != word[0] or word in prev_words:
            if (i+1)%n ==0:
                number = n;
            else:
                number = (i+1)%n;
            answer = [number,i//n+1];
            break;
        prev_word = word[-1];
        prev_words[word] = 0;
    if len(answer) == 0:
        return [0,0]
    else:
        return answer