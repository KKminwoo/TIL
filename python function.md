## 0. heapq 라이브러리
- 우선순위 큐 알고리즘
- 이진 트리 기반의 최소 힙 자료구조를 모듈로 제공
```python
import heapq
list = [1,2,3,4]

# 리스트를 heap 구조로 변형
heapq.heapify(list)

# heap에 요소 추가하기
heapq.heappush(list,3)

# heap 요소 삭제하기
heapq.heappop(list,3)
```

## 1. join 함수

- 리스트를 문자열로 합쳐주는 함수

```python
def solution(s):
    return ''.join(sorted(s, reverse=True))

solution('Zbcdefg')
# gfedcbZ
```

## 2. isdigit 함수, is_integer 함수
- isdigit : 문자열이 정수인지 확인하는 함수
- is_integer : float 값이 정수인지 확인하는 함수
```python
if s.isdigit() == True:
    return True
if s.is_integer() == True:
    return True
```

## 3. enumerate 함수
```python
for i,num in enumerate(seoul):
    print(i,num)
    # i = 내용, num = 숫자
```

## 4. 아스키 코드 변화
- ord(문자) : 아스키 코드를 반환
- chr(숫자) : 숫자에 맞는 아스키 코드를 반환
```python
print(chr(45))
print(ord("a"))
```

## 5. map 함수
- 리스트의 요소를 지정된 함수로 처리해주는 것
- list(map(함수,리스트))
```python
def digit_reverse(n):
    return list(map(int, str(n)))
```

## 6. math import
- sqrt : 제곱근 구해주는 함수
- gcd : 최대공약수
- ceil : 올림
- floor : 내림
- round : 반올림
```python
import math
def solution(n,m):
    return math.sqrt(n)
    return math.gcd(n,m)
```

## 7. split 함수
- 공백 기준 문자열을 분리해 리스트로 저장하는 함수
```python
def solution(n):
    return n.split()
```
