## heapq 라이브러리
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

## deque 라이브러리
- 양방향 큐 : 앞, 뒤 양쪽 방향에서 요소를 추가하거나 제거 가능
- 일반적인 리스트가 O(n)이 소요되는 반면 deque는 O(1)로 접근 가능하다.
```python
from collections import deque

deq = deque()

# 앞에 요소 삽입
deq.appendleft(10)

# 끝에 요소 삽입
deq.append(10)

# 앞에 요소 제거
deq.popleft()

# 끝에 요소 제거
deq.pop()
```
## Counter 함수(collections 라이브러리)
- 리스트에서 특정 요소 빈도 추출해내는 함수

```python
from collections import Counter
m = [1,1,1,1,2,2,2,3,3,4]
counter_list = Counter(m).most_common() # 빈도수가 큰 값대로 순서대로 딕셔너리 형태로 저장
print(counter_list)
# [(1,4),(2,3),(3,2),(4,1)]
```

## Combinations 함수(itertools 라이브러리)
- 리스트에서 조합을 뽑는 함수

```python
from itertools import combinations
m = [1,2,3,4]
for i in list(combinations(m,2):
    print(i)
    # 리스트에서 2개 조합 출력
```

## isdigit 함수, is_integer 함수, isalpha 함수, isalnum 함수
- isdigit : 문자열이 정수인지 확인하는 함수
- is_integer : float 값이 정수인지 확인하는 함수
- isalpha : 문자열이 알파벳인지 확인하는 함수
- isalnum : 문자열이 알파벳 또는 정수인지 확인하는 함수
```python
if s.isdigit():
    return True
if s.is_integer():
    return True
if s.isalpha():
    return True
if s.isalnum():
    return True
```

## enumerate 함수
```python
for i,num in enumerate(seoul):
    print(i,num)
    # i = 내용, num = 숫자
```

## 아스키 코드 변화
- ord(문자) : 아스키 코드를 반환
- chr(숫자) : 숫자에 맞는 아스키 코드를 반환
```python
print(chr(45))
print(ord("a"))
```

## map 함수
- 리스트의 요소를 지정된 함수로 처리해주는 것
- list(map(함수,리스트))
```python
def digit_reverse(n):
    return list(map(int, str(n)))
```

## math import
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

## split 함수
- 공백 기준 문자열을 분리해 리스트로 저장하는 함수
```python
def solution(n):
    return n.split()
```
