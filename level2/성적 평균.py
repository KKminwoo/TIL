N = input().split()[1] # 학생 수

for i in range(int(N)+1):
    if i == 0: # 학생 성적 입력
        num = list(map(int,input().split()))
    else:
        ran = list(map(int,input().split()))
        div = num[ran[0]-1:ran[1]]
        ans = sum(div)/len(div)
        print('%.2f' %ans)
