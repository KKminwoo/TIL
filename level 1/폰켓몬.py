# my solution
def solution(nums):
    answer = len(nums)/2 # 가져가는 폰켓몬 수
    nums = len(set(nums)) # 폰켓몬 종류 수
    if answer > nums:
        answer = nums
    return answer
  
# excellent solution
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
