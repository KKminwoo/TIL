# wrong solution
def solution(numbers, hand):
    answer = ''
    l_hand = 10
    r_hand = 12
    for j in range(len(numbers)):
      if numbers[j] == 0:
        numbers[j]=11
    for i in numbers:
      if i in [1,4,7]:
        answer = answer + "L"
        l_hand = i # 1 4
      elif i in [3,6,9]:
        answer = answer + "R"
        r_hand = i # 3
      else:
        print()
        if abs(i - (l_hand + 2)) < abs(i - r_hand): # 0
          if abs(i-r_hand) == 3:
            r_hand = id
            answer = answer + "R"
          else:
            l_hand = i
            answer = answer + "L"
        elif abs(i - l_hand + 2) > abs(i - r_hand): # 7
          if abs(i-l_hand) == 3:
            l_hand = i
            answer = answer + "L"
          else:
            r_hand = i
            answer = answer + "R"
        else:
          answer = answer + hand[0].upper()
    return answer

# right solution
def solution(numbers, hand):
    answer = ''
    lastL = 10
    lastR = 12
    
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            lastL = n
        elif n in [3,6,9]:
            answer+='R'
            lastR = n
        else:
            n = 11 if n == 0 else n
            
            absL = abs(n-lastL)
            absR = abs(n-lastR)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer+='R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                lastL = n
            else:
                if hand == 'left':
                    answer+='L'
                    lastL = n
                else:
                    answer+='R'
                    lastR = n
                
    return answer
