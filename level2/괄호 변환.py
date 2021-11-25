def solution(p):
    answer = ''
    num = 0
    for i in p:
        if i == "(":
            num += 1
        else:
            num -= 1
        
    return answer
