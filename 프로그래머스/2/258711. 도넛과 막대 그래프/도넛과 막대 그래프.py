def solution(edges):
    answer = [0,0,0,0];
    
    exchangeCnts = {}
    for a,b in edges:
        if a not in exchangeCnts:
            exchangeCnts[a] = [0,0];
        if b not in exchangeCnts:
            exchangeCnts[b] = [0,0];
        # 나가는 선
        exchangeCnts[a][0] += 1;
        # 들어오는 선
        exchangeCnts[b][1] += 1;
    for key, count in exchangeCnts.items():
        # 생성된 정점
        if count[0]>=2 and count[1] == 0:
            answer[0] = key;
        # 막대그래프
        elif count[1]>0 and count[0]==0:
            answer[2] += 1;
        # 8자그래프
        elif count[0] >= 2 and count[1]>=2:
            answer[3] += 1;
            
    answer[1] = (exchangeCnts[answer[0]][0] - answer[2] - answer[3]);
    return answer