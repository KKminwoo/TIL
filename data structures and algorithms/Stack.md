## 1. 스택 구조

- 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조
- LIFO(Last In First Out) 또는 FILO(First In Last Out)
- push(): 데이터를 스택에 넣기
- pop(): 데이터를 스택에서 꺼내기

<img src="http://www.fun-coding.org/00_Images/stack.png" />

## 2. 스택 구조와 프로세스 스택

```python
# 재귀 함수
def recursive(data):
	if data < 0:
		print("ended")
	else:
		print(data)
		recursive(data-1)
		print("return",data)

<!-- 
4
3
2
1
0
ended
returned 0
returned 1
returned 2
returned 3
returned 4
-->
```

## 3. 자료구조 스택의 장단점

- 장점
구조가 단순해서 구현이 쉽다.
데이터 저장/읽기 속도가 빠르다
- 단점(일반적인 스택 구현시)
데이터 최대 갯수를 미리 정해야 한다.(파이썬의 경우 재귀함수 1000번까지 호출이 가능)
저장 공간의 낭비가 발생할 수 있다.(미리 최대 갯수만큼 저장공간을 확보해야 함)

## 4. 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용

```python
# append(push), pop 메서드 제공

data_stack = list()

data_stack.append(1)
data_stack.append(2)
# [1,2]

data_stack.pop() # 가장 마지막 데이터 출력
# 2
```

## 5. 리스트 변수로 스택을 다루는 pop, push 기능 구현

```python
stack_list = list()

def push(data):
	stack_list.append(data)
def pop():
	data = stack_list[-1]
	del stack_list[-1]
	return data
```
