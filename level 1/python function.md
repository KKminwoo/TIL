### join 함수

- 리스트를 문자열로 합쳐주는 함수

```python
def solution(s):
    return ''.join(sorted(s, reverse=True))

solution('Zbcdefg')
# gfedcbZ
```

### isdigit 함수
- 문자열이 정수인지 확인하는 함수
```python
if s.isdigit() == True:
    return True
```

### enumerate 함수
```python
for i,num in enumerate(seoul):
    print(i,num)
    # i = 내용, num = 숫자
```

### 아스키 코드 변화
- ord(문자) : 아스키 코드를 반환
- chr(숫자) : 숫자에 맞는 아스키 코드를 반환
```python
print(chr(45))
print(ord("a"))
```
