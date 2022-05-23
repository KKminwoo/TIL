num = list(map(int, input().split())) # W, N 입력
count = []
weight = []
for i in range(num[1]):
    index = list(map(int, input().split()))
    weight.append(index[0]) # [90, 70]
    count.append(index[1]) # [1,2]

while num[0] > 0:
    if num[0] < weight[count.index(max(count))]: # 귀금속 금액이 배낭 무게보다 높을 경우
        ans += num[0]*max(count)
        num[0] -= weight[count.index(max(count))]
        print(ans)

    else:
        ans = weight[count.index(max(count))] * max(count)
        num[0] -= weight[count.index(max(count))]
        weight.remove(weight[count.index(max(count))])
        count.remove(max(count))
    
