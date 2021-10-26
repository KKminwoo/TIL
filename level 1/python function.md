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
