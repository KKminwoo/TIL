import math
def solution(progresses, speeds):
    answer = []
    left_day = []
    flag = 0
    num = 1
    # 남은 일자 계산하기
    for i in range(len(progresses)):
        left_day.append(math.ceil((100-progresses[i])/speeds[i]))
    # 베포 순서
    for value in left_day:
        if value > flag:
            flag = value
            answer.append(num)
            num = 1
        else:
            num += 1
    answer.append(num)
    return answer[1:]
