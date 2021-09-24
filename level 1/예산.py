# my solution
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            break
        else:
            answer += 1
    return answer
  
# right solution
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
