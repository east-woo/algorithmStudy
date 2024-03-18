#2512. 예산
#이분탐색
N = int(input())
req = list(map(int, input().split))
M = int(input())

lo = 0
hi = max(req)
mid = (lo+hi) // 2
ans = 0

def is_possible(mid):

while lo <= hi:
    if is_possible(mid):
        lo = mid+1


print(ans)