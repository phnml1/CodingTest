def solution(word):
    default_words,words = ['A','E','I','O','U'],[];
    answer = -1;
    def dfs(n, w):
        nonlocal answer;
        words.append(w);
        if w == word:
            answer = len(words);
            return;
        if n==5 or answer != -1:
            return;
        for i in default_words:
            dfs(n+1, w+i);
    for w in default_words:
        dfs(1,w)
    return answer