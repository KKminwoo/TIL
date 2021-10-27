def solution(s):
    answer = ''
    num=0
    for i in range(len(s)):
        if s[i] == ' ':
            num=0
            answer += ' '
            pass
        else:
            if num==0:
                answer += s[i].upper()
                num=1
            else:
                answer += s[i].lower()
                num=0
    return answer

