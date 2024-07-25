# 문제 자연수 N과 정수 K가 주어졌을 때 이항 계수 binom{N}{K}를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)
#
# 출력
# binom{N}{K}를 10,007로 나눈 나머지를 출력한다.

## 재귀 (top-down)
import sys
sys.setrecursionlimit(10**7)
N, K = map(int,input().split())
mod = 10_007
cache=[[0]*1001 for _ in range(1001)]

def bino(n,k):
    if cache[n][k]:
        return cache[n][k]

    if k==0 or k==n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
        cache[n][k] %= mod

    return cache[n][k]

print(bino(N,K))

## 반복 (bottom-up)
# mod = 10_007
# cache=[[0]*1001 for _ in range(1001)]
# N, K = map(int,input().split())
#
# for i in range(1001):
#     cache[i][0] = cache[i][i] = 1
#     for j in range(1,i):
#         cache[i][j] = cache[i-1][j-1]+cache[i-1][j]
#
# print((cache[N][K])%mod)