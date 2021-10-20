def solution(arr):
    num = -1
    answer = []
    for i in arr:
        if num == i:
            pass
        else:
            answer.append(i)
        num = i
    return answer
