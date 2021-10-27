# my solution
def solution(n):
    answer = []
    for i in range(1,len(str(n))+1):
        answer.append(int(str(n)[len(str(n))-i]))
    return answer

# right solution
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
