def solution(new_id):
    word = '~!@#$%^&*()=+[{]}:?,<>/'
    # 1단계
    answer = new_id.lower()
    # 2단계
    for i in range(len(word)):
      answer = answer.replace(word[i],"")
    # 3단계
    while ".." in answer:
      answer = answer.replace("..",".")
    # 4단계
    if answer[0]==".":
      answer = answer[1:]
    if len(answer) > 1:
      if answer[len(answer)-1] == ".":
        answer = answer[:len(answer)-1]   
    # 5단계
    if len(answer) == 0:
      answer = "a"
    # 6단계
    if len(answer) >= 16:
      answer = answer[:15]
      if answer[len(answer)-1] == ".":
        answer = answer[:len(answer)-1]   
    # 7단계
    if len(answer) < 3:
      answer = answer + (3-len(answer))*answer[len(answer)-1]
    return answer
