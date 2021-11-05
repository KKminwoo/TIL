# 수학적 사고 활용 문제.
# 알고리즘을 더 간단한 코딩으로 풀어낼 수 있도록 생각을 하자

import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w,h))
