# My solution
def solution(scores):
    answer = ''
    for i in range(len(scores)):
        list = []
        # 요소 합 구하기
        average = 0
        for j in range(len(scores[i])):
            average += scores[j][i]
            list.append(scores[j][i])
        # 평균 구하기
        if list[i] == max(list) and list.count(max(list))==1:
            average = (average - scores[i][i]) / (len(scores[i])-1)
        elif list[i] == min(list) and list.count(min(list))==1:
            average = (average - scores[i][i]) / (len(scores[i])-1)            
        else:
            average = average / len(scores[i])
        # 등급 나누기
        if average >= 90:
            answer += 'A'
        elif average >= 80 and average < 90:
            answer += 'B'
        elif average >= 70 and average < 80:
            answer += 'C'
        elif average >= 50 and average < 70:
            answer += 'D'
        else:
            answer += 'F'
    return answer

# Right solution
def solution(scores) :
    avgs=[]
    score=[ [i[j] for i in scores] for j in range(len(scores))]

    for idx,i in enumerate(score) :

        avg=sum(i) ; length=len(i)

        if i[idx] == max(i) or i[idx] == min(i) :

            if i.count(i[idx]) == 1 :

                avg-=i[idx] ; length-=1

        avgs.append(avg/length)

    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])
