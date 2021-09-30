# my solution
def solution(answers):
    way = [[1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    right_count = []
    answer = []
    num = 0
    for i in range(3):
        for j in range(len(answers)):
            way[i] = way[i]*(len(answers)//len(way[i])+1)
            if answers[j] == way[i][j]:
                num += 1
        right_count.append(num)
        num=0
    # enumerate 체크하기! -> 리스트의 인덱스와 값을 동시에 출력해주는 함수
    for person, index in enumerate(right_count):
        if index == max(right_count):
            answer.append(person+1)
    return answer
