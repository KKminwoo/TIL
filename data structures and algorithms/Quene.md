## 1. 큐의 구조

- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
FIFO(First In, First Out), 줄을 선 사람이 제일 먼저 입장하는 것과 동일

<img src="https://www.fun-coding.org/00_Images/queue.png" />

## 2. 용어

- Enqueue : 큐에 데이터를 넣는 기능
- Dequeue : 큐에서 데이터를 꺼내는 기능

## 3. 파이썬 queue 라이브러리

### 3-1. Queue()로 큐 만들기

```python
import queue
data_queue = queue.Queue()

# 데이터 넣기
data_queue.put("hello")
data_queue.put(1)

# 데이터 빼기
data_queue.get()
# -> 'hello'
```

### 3-2 LifoQueue()로 큐 만들기(LIFO Last In First Out)

```python
import queue
data_queue = queue.LifoQueue()

data_queue.put('hello')
data_queue.put(1)

data_queue.get()
# -> 1
```

### **3-3 PriorityQueue()로 큐 만들기**

```python
import queue
data_queue = queue.PriorityQueue()

data_queue.put((10,"korea")) # 튜블 형식으로 넣어줌
data_queue.put((5,1))
data_queue.put((15,'china'))

data_queue.qsize()
# 3

data_queue.get() # 우선순위가 높은(숫자가 낮은) 값을 출력
# (5,1)
data_queue.get()
# (10,"korea")
```

### ※ 리스트 변수로 큐를 다루는 기능 구현

```python
queue_list = list()

def enqeue(data):
	queue_list.append(data)

def deqeue():
	data = queue_list[0]
	del queue_list[0]
	return data
```
