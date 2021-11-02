# 수학적 사고 기르자.
# 틀린 문제

import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w,h))
