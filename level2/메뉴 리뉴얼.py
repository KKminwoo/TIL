# Counter 함수 익히기
# combination 함수 익히기

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    counter_num = {}
    for j in course:
        count_list = []
        for i in orders:
            for k in list(combinations(i,j)):
                count_list.append(''.join(sorted(k)))
        counter_num = Counter(count_list).most_common()
        for s in counter_num:
            if counter_num[0][1] > 1 and s[1] == counter_num[0][1]:
                print(counter_num[0][1], s[0])
                answer.append(s[0])
    return sorted(answer)
