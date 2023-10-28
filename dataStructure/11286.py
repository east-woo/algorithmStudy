import heapq as hq
import sys

input = sys.stdin.read
pq= []

for _ in range(int(input())):
    x = input()
    if x:
        hq.heappush(pq,(abs(x),x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)