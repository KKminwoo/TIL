# My solution -> 효율성 테스트 통과 x
def solution(scoville, K):
    answer = 0
    for i in range(len(scoville)):
        if min(scoville) >= K:
            return answer
        elif len(scoville) < 2:
            return -1
        else:
            scoville = sorted(scoville)
            scoville.append(scoville[0]+scoville[1]*2)
            scoville = scoville[2:]
            answer += 1
        print(scoville.index(min(scoville)))       

        
