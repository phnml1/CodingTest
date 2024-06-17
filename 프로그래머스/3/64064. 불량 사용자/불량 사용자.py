from itertools import permutations;
from collections import defaultdict
answer = 0
def compare(user_word,ban_word):
    if len(user_word) != len(ban_word):
        return False;
    
    for i in range(len(user_word)):
        if user_word[i] != ban_word[i]:
            if ban_word[i] != '*':
                return False;
    return True;
def solution(user_id, banned_id):
    ban_set = []
    for case in list(permutations(user_id, len(banned_id))):
        case = list(case);
        flag = True;
        for i in range(len(case)):
            if compare(case[i],banned_id[i]) == False:
                flag = False;
                break;
        if flag:
            case = set(case);
            if case not in ban_set:
                ban_set.append(case);
    return len(ban_set)