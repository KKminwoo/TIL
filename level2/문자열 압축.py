# not solve
def solution(s):
    num = s[0]
    count = 0
    word = ''
    answer = []
    for i in s:
        if i==num:
            count += 1
            num = i
            # print(i,"coount 1")
        else:
            if count <= 1:
                word += num
                # print(num'one arg')
            else:
                word = word + str(count) + num
            num = i
            count = 1
        print(word)
            
    return answer
