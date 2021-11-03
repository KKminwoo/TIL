def solution(n):
    answer = ''
    if n <= 3:
        answer = '124'[n-1]
    else:
        n -= 1
        answer =  + '124'[n%3]
        
    
    return answer


# 11 42
# 12 44
# 13 111
# 14 112
