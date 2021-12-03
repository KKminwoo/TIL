from itertools import permutations

def solution(numbers):
    answer = 0
    for i in range(1,len(numbers)+1):
        for k in list(list(permutations(numbers,i))):
            print(k)
    return answer
