# perfect solution
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
 
# my solution
def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price*i
    if answer-money <= 0:
        return 0
    else:
        return answer-money
