# Right Solution
def solution(weights, head2head):
    answer = []
    result = []
    for i in range(len(head2head)):
        w = 0
        l = 0
        cnt = 0
        head2head[i] = list(head2head[i])
        for j in range(len(weights)):
            if head2head[i][j] == 'W':
                w += 1
                if weights[i] < weights[j]:
                    cnt += 1
            elif head2head[i][j] == 'L':
                l += 1
        if w+l != 0:
            result.append([i+1, w/(w+l), cnt, weights[i]])
        else:
            result.append([i+1, 0, cnt, weights[i]])
    result.sort(reverse=True, key = lambda x : (x[1],x[2],x[3]) )
    for i in range(len(result)):
        answer.append(result[i][0])
    return answer
