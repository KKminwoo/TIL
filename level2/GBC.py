from collections import deque

count = list(map(int, input().split()))
max_diff = 0
deq1 = deque()
deq2 = deque()

for i in range(count[0]):
    deq1.append(list(map(int,input().split())))

for j in range(count[1]):
    deq2.append(list(map(int,input().split())))

while len(deq2)>0:
    if deq1[0][0] < deq2[0][0]:
        if max_diff < deq2[0][1]-deq1[0][1]:
            max_diff = deq2[0][1]-deq1[0][1]
        k = [deq2[0][0]-deq1[0][0],deq2[0][1]]
        deq1.popleft()
        deq2.popleft()
        deq2.appendleft(k)
    elif deq1[0][0] > deq2[0][0]:
        if max_diff < deq2[0][1]-deq1[0][1]:
            max_diff = deq2[0][1]-deq1[0][1]
        k = [deq1[0][0]-deq2[0][0],deq1[0][1]]
        deq1.popleft()
        deq2.popleft()
        deq1.appendleft(k)
    else:
        if max_diff < deq2[0][1]-deq1[0][1]:
            max_diff = deq2[0][1]-deq1[0][1]
        deq1.popleft()
        deq2.popleft()

print(max_diff)
