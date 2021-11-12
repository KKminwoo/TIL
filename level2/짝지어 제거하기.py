# 잘 풀었지만 좀 더 자료구조 알고리즘 익숙해지기

from collections import deque
def solution(s):
    deq = deque()
    deq.append(s[0])
    for i in range(1,len(s)):
        if len(deq) == 0 or deq[len(deq)-1] != s[i]:
            deq.append(s[i])
        else:
            deq.pop()
    return 1 if len(deq) == 0 else 0
