import copy;
def rotate90(key):
    new_key = copy.deepcopy(key);
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[i][j] = key[len(key)-1-j][i];
    return new_key;

def check(key,board,x,y,M,N):
    answer = True;
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j];

    for i in range(M,M+N):
        for j in range(M,M+N):
            if board[i][j] != 1:
                answer = False;
                break;
                
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j];
    return answer;
                
def solution(key, lock):
    N,M = len(lock),len(key);
    board = [[0 for _ in range(N + 2*M)] for _ in range(N + 2*M)];
    for i in range(N):
        for j in range(N):
            board[i+M][j+M] = lock[i][j];
    for i in range(4):
        key = rotate90(key);
        for i in range(M+N):
             for j in range(M+N):
                if check(key,board,i,j,M,N):
                    return True;
    return False;