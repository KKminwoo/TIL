def solution(board, moves):
  result = []
  answer = 0
  for i in moves:
    for j in range(len(board)):
      if board[j][i-1] is not 0:
        result.append(board[j][i-1])
        if len(result)>1 and result[len(result)-2] == result[len(result)-1]:
          del(result[len(result)-2])
          del(result[len(result)-1])
          answer += 2
        board[j][i-1] = 0
        break
  return answer
