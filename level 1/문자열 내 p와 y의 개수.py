# my solution
def solution(s):
    answer = True
    if s.count("p")+s.count("P") == s.count("y")+s.count("Y"):
        return True
    elif s.count("p")+s.count("P") == 0 and s.count("y")+s.count("Y")==0:
        return True
    else:
        return False
      
# right solution
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
