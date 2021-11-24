from itertools import combinations

def solution(orders, course):
    answer = []
    max_num = 0
    for j in course:
        count_list = []
        print(j,"개 선택")
        for i in orders:
            for k in list(combinations(i,j)):
                count_list.append(''.join(k))
                if ''.join(k) in count_list and count_list.count(''.join(k)) >= max_num:
                    print(''.join(k),count_list.count(''.join(k)))
                    max_num = count_list.count(''.join(k))
                print(count_list)
    return answer
