def solution(s, n):
    answer = ''
    lo = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # print(lower.find(s[0]))
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper() == True:
            answer += up[(up.find(i)+n)%26]
        elif i.islower() == True:
            answer += lo[(lo.find(i)+n)%26]
    return answer
