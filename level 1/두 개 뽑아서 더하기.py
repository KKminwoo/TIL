import itertools
def solution(numbers):
    answer = []
    nCr = itertools.combinations(numbers,2)
    print(nCr)
    return answer
