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

        
# heap 알고리즘을 활용한 코드
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2 and scoville[0] < K:
            return -1
        else:
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
            answer += 1
    return answer
