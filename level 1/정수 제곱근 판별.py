import math
def solution(n):
    answer = 0    
    if (math.sqrt(n)).is_integer():
        return ((math.sqrt(n))+1)**2
    else:
        return -1
