def solution(participant, completion):
  participant.sort()
  completion.sort()
  for i in completion:
    if i in participant:
      participant.remove(i)

  answer = participant[0]
  return answer
