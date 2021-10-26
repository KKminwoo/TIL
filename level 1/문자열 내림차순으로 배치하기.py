# my solution
def solution(s):
    answer = ''
    list = []
    for i in s:
        list.append(ord(i))
    list.sort(reverse = True)
    for j in list:
        print(chr(j))
        answer += chr(j)
    return answer


# right solution
# ''.joint() 함수 숙지하기
def solution(s):
    return ''.join(sorted(s, reverse=True))
