# 실패율 구하기 성공, 오름차순으로 나타내기 실패
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
    for index, rank in enumerate(answer):
        if rank == max(answer):
            # answer.append(index+1)
            print(index+1,rank)
    return answer

# 성공 코드
def solution(N, stages):
    fail_rate = {}
    total_user = len(stages)

    for stage in range(1, N+1):
        if total_user != 0:
            fail_user = stages.count(stage)
            fail_rate[stage] = fail_user / total_user
            total_user -= fail_user
        else:
            fail_rate[stage] = 0

    return sorted(fail_rate, key=lambda x : fail_rate[x], reverse=True)
