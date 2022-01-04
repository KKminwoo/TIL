from itertools import permutations

def solution(expression):
    answer = 0
    operator = ['*','-','+']
    # 식의 연산자 파악
    for i in operator:
        if i not in expression:
            operator.remove(i)
    for i in permutations(operator,2):
        print(i)
    return answer
