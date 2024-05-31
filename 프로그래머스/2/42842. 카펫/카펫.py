import math
def solution(brown, yellow):
    for j in range(1,int(math.sqrt(yellow))+1):
        c,r = 0,0
        if yellow % j ==0:
            r = j
            c = yellow//j
            if brown == 2*c + 2*r + 4:
                return [2+c,2+r];