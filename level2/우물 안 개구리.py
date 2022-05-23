count = list(map(int,input().split()))[1] # 집합 수
weight_list = list(map(int,input().split())) # 무게 리스트
ans = []
for i in range(count):
    ran = list(map(int,input().split()))
    if weight_list[ran[0]-1] > weight_list[ran[1]-1]:
        ans.append(ran[0])
    elif weight_list[ran[0]-1] < weight_list[ran[1]-1]:
         ans.append(ran[1])
print(len(set(ans)))
