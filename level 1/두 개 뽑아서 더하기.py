# my solution
import itertools
def solution(numbers):
    answer = set()
    nCr = itertools.combinations(numbers,2)
    for i in list(nCr):
        answer.add(sum(i))
    return sorted(answer)

# right solution (wow~)
from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))
