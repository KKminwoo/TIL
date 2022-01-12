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
```
