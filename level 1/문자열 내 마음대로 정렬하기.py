# lambda 함수 기억하기!!
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])
