def solution(absolutes, signs):
    answer = 0
    k=0
    for i in signs:
      if i > 0:
        answer += absolutes[k]
        k += 1
      else:
        answer -= absolutes[k]
        k += 1
    return answer
