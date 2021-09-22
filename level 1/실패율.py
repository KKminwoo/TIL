def solution(N, stages):
    in_stage_count = 0
    not_clear_count = 0
    answer = []
    for i in range(1,N+1):
        for j in range(len(stages)):
            if stages[j]>i:
                in_stage_count += 1
            elif stages[j]==i:
                not_clear_count += 1 
        answer.append(not_clear_count/in_stage_count)
                
        
    return answer

#1 -> 1/8
#2 -> 3/7
#3 -> 2/4
#4 -> 1/2
#5 -> 0/1
