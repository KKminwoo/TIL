from itertools import combinations

def solution(orders, course):
    answer = []
    count = []
    for j in course:
        print(j,"개 선택")
        for i in orders:
            for k in list(combinations(i,j)):
                if 
                count.append(k)
        print(count)
            # print("\n")
    return answer
