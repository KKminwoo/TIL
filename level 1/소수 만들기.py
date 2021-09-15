import itertools

def solution(nums):
    answer = 0
    k=0
    nCr = itertools.combinations(nums,3) # 조합 뽑기
    for i in list(nCr):
      for j in range(1,sum(i)+1):
        if sum(i)%j==0:
          k += 1
      if k == 2:
        answer += 1
      k=0
    return answer
