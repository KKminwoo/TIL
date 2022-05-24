number = {'0':1110111, '1':10010, '2':1011101, '3':1011011, '4':111010, 
'5':1101011, '6':1101111, '7':1110010, '8':1111111, '9':1111011 } # 숫자 이진화

count = int(input()) # 입력 횟수

for i in range(count):
    before, after = input().split()
    ans = 0
    
    for j in range(min(len(before),len(after))): 
        change = str(number.get(str(before[-1-j])) + number.get(str(after[-1-j]))).count('1') # 각자리 이진화숫자 합 중 변경된 횟수
        ans += change

    # 자릿수가 차이날 경우 해당 숫자만큼 추가
    if len(before) > len(after):
        for k in range(len(before) - len(after)):
            change = str(number.get(before[k])).count('1')
            ans += change
            
    elif len(before) < len(after):
        for k in range(len(after) - len(before)):
            change = str(number.get(after[k])).count('1')
            ans += change

    print(ans)
