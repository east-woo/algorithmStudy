import sys
from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
chk = [[False] * 100 for _ in range(100)]

N = 3

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True
        print(f"{x}, {y}")
        print(f"Visiting: ({x}, {y})")  # 방문한 좌표 출력

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))
                chk[ny][nx] = True  # 새로운 좌표를 큐에 넣을 때 방문 체크도 함께 해야 함
                print(f"{nx}, {ny}")
bfs(0, 0)
