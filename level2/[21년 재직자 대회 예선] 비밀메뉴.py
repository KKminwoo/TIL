num = list(map(int, input().split())) # 입력 값 리스트로 저장

key = input().replace(" ","") # 비밀 메뉴 조작법

arry = input().replace(" ","") # 사용자 버튼 조작

if num[0] > num[1]:
    print('normal')
else:
    for i in range(num[1]):
        if key == arry[i:i+num[0]]:
            print('secret')
            break
        elif i+num[0] == num[1]:
            print('normal')
            break
