# my solution
def solution(n):
    reverse = []
    answer = 0
    while n > 0:
        reverse.append(n%3)
        n=n//3
    for i in range(len(reverse)):
        answer += 3**(len(reverse)-1-i)*reverse[i]
    return answer

# right solution(wow!)
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
