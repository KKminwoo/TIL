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


