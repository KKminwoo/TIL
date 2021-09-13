def solution(board, moves):
  result = []
  for i in moves:
    for j in range(len(board)):
      if board[j][i-1] is not 0:
        result.append(board[j][i-1])
        board[j][i-1] = 0
        print(result)
        break
  # while True:
  for j in range(len(result)):
    print(result[j],result[j+1])
    # if result[j] == result[j+1]:
    #   result = result.remove(result[j])
  print(result)
  return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],	[1,5,3,5,1,2,1,4])
