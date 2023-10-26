## 2164번 카드
## https://www.acmicpc.net/problem/2164

### 큐
from collections import deque

N = int(input())
dq = deque(range(1,N+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())

### 배열 X

# N = int(input())
# arr = [*range(1,N+1)]
#
# while len(arr) > 1:
#     arr.pop(0)
#     arr.append(arr.pop(0))
#
# print(arr.pop(0))