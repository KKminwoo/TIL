from collections import deque

count = int(input())

deq = deque()

for i in range(count):
    num = input().replace(" ","")
    if len(deq) == 0:
        deq.append(num)
    else:
        if int(deq[-1][1]) <= int(num[0]):
            deq.append(num)
        else:
            pass
print(len(deq))
