def solution(bandage, health, attacks):
    answer = 0;
    t = attacks[-1][0];
    max_health = health;
    next_attack,bandage_time = 0,0;
    for i in range(t+1):
        if i == attacks[next_attack][0]:
            health -= attacks[next_attack][1];
            next_attack += 1;
            bandage_time = 0;
            if health<=0:
                return -1
            continue;
        if health<max_health:
            bandage_time += 1;
            health = min(health+bandage[1],max_health);
            if bandage_time == bandage[0]:
                health = min(health+bandage[2],max_health);
                bandage_time=0;
        
            
    return health