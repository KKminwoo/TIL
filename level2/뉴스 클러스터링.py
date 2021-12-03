from collections import Counter

def solution(str1, str2):
    answer = 0
    a = []
    # str1 2개 뽑기
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            a.append(str1[i:i+2].upper())
    # str2 2개 뽑기
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            a.append(str2[i:i+2].upper())
    a = Counter(a).most_common()
    print(a)
    for j in a:
        if j[1]>1:
            answer += 1
    return 65536 if len(a) == 0 else 65536*(answer/len(a))
