## 그리디 문제
## 11047. 동전 0
## https://www.acmicpc.net/problem/11047


N, K = map(int, input().split())
coins =[int(input()) for _ in range(N)]
coins.reverse()
ans = 0
c=0
for coin in coins:
    ans += K // coin
    K %= coin

    print(ans)
