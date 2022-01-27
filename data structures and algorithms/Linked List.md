## 1. 링크드 리스트의 구조

- 연결 리스트라고도 하며, 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
→ 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원
- 노드 : 데이터 저장 단위(데이터값, 포인터)로 구성

![Untitled](https://user-images.githubusercontent.com/47807421/151315583-8397c830-61e3-47e1-a91f-4a05278eb1b4.png)

- 포인터 : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

## 2. 링크드 리스트 예

- 노드 구현

```python
class Node:
	def__init__(self, data):
		self.data = data
		self.next_data=None
```

```python
# 좀 더 자세하게 적은 클래스
# 주소값을 넣지 않을 경우 default 값으로 None이 들어간다
class Node:
	def__init__(self.data,next_data=None):
		self.data= data
		self.next_data = next_data
```

- 링크드 리스트로 데이터 추가

```python
class Node:
	def__init__(self.data,next_data=None):
		self.data= data
		self.next_data = next_data

def add(data):
	node = head
	while node.next_data:
		node = node.next_data
	node.next_data = Node(data)
```

```python
# 두 개의 노드를 만들어 링크드 리스트 구현
node1 = Node(1)
head = node1
for index in range(2,10):
	add(index)
```

- 링크드 리스트 데이터 출력하기

```python
node = head
while node.next_data:
	print(node.data)
	node = node.next_data
print(node.data)

<!--
1
2
3
4
5
6
7
8
9
-->
```

## 3. 링크드 리스트의 장단점

- 장점
미리 데이터 공간을 할당하지 않아도 됨
(배열은 미리 연결된 데이터 공간을 할당해야 함)
- 단점
연결을 위한 별도 주소 데이터 공간이 필요해 효율이 높지 않음
연결 정보를 찾는 시간이 걸려 접근 속도가 느림
중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 함

## 4. 링크드 리스트 데이터 사이에 데이터를 추가

<img src="https://www.fun-coding.org/00_Images/linkedlistadd.png" />

```python
node = head
while node.next_data:
	print(node.data)
	node = node.next_data
print(node.data)

<!--
1
2
3
4
5
6
7
8
9
-->
```

```python
node3 = Node(1.5) # 1과 2사이에 데이터를 추가
```

```python
node = head
search = True
while search:
	if node.data == 1:
		search = False
	else
		node = node.next_data

node_next = node3 # 가리키는 주소 값을 2가 아니라 1.5로 변경
node3.next_data = node_next

<!--
1
1.5
2
3
4
5
6
7
8
9
-->
```

## 5. 파이썬 객체지향 프로그램으로 링크드 리스트 구현

```python
class Node:
	def __init__(self.data,next_data = None):
		self.data = data
		self.next_data = next_data

class NodeMgmt:
	def add(self,data):
	def(desc(self)
```
