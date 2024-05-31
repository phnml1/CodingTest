def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack)==0:
            stack.append(i);
        elif i == ')' and stack[-1] == '(':
            stack.pop(-1);
        else:
            stack.append(i);
    if len(stack)>0:
        return False;
    else:
        return True