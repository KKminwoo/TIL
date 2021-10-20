# My Solution
def solution(n, arr1, arr2):
    answer = []
    i=0
    while i<n:
        sum = str(int(bin(arr1[i])[2:])+int(bin(arr2[i])[2:]))
        if len(sum) < n:
            sum = "0"*(n-len(sum))+sum
        print(sum)
        answer.append(sum)
        answer[i] = answer[i].replace("1","#")
        answer[i] = answer[i].replace("2","#")
        answer[i] = answer[i].replace("0"," ")
        i += 1
    return answer
  
# Good Solution
# rjust(width, [fillchar]) 함수 사용
# "2".rjust(3, "0") -> "002"

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
