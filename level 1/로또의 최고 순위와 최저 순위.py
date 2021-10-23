# my solution
def solution(lottos, win_nums):
    answer = []
    count = lottos.count(0) # 0 갯수 파악
    same_num = 0
    for i in lottos:
      for j in win_nums:
        if i == j:
          same_num += 1
        else:
          pass
      if same_num == 0:
        answer=[7-same_num-count,6]
        if count == 0:
          answer=[6,6]
      else:
        answer = [7-same_num-count,7-same_num]
    return answer


# 훌륭한 코드
# 랭크 리스트를 미리 만들어두는 방식!! 와우
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return rank[cnt_0 + ans],rank[ans]
