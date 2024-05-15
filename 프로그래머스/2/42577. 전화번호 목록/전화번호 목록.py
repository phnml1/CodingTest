def solution(phone_book):
    answer = True;
    phone_book.sort();
    for i in range(len(phone_book)-1):
        result = False;
        for j in range(len(phone_book[i])):
            if phone_book[i][j] != phone_book[i+1][j]:
                result = True;
                break;
        if result == False:
            answer=False;
            break;
        
    return answer