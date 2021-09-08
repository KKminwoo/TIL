'''
"one4seveneight" -> 1478
"23four5six7" -> 234567
"2three45sixseven" -> 234567
"123" -> 123
'''

# first try. wrong solution
def pre_solution (s):
  number = ['zero','one','two','three','four','five','six','seven','eight','nine']
  int_number = ['0','1','2','3','4','5','6','7','8','9']
  i = 0
  f = 0
  answer = []
  for k in range(10):
    for j in range(len(number[k])):
      if i == len(s):
        break
      elif s[i] == number[k][j]:
        f += 1
        # print(int_number[k])
        # print("if",i)
        i += 1
        if f==len(number[k]):
          answer.append(str(k))
          f=0
      elif s[i] == int_number[k]:
        # print(int_number[k])
        answer.append(str(k))
        i += 1
        # print("elif",i)
      else:
        i -= f
        f = 0
        # print(k,"wrong")
        break
  return int("".join(answer))

# second try. right solution
def solution(s):
  number = ['zero','one','two','three','four','five','six','seven','eight','nine']
  for i in number:
    s = s.replace(i,str(number.index(i)))
  return int(s)
