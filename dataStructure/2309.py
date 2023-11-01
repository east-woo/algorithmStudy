# 2309. 일곱난쟁이
from itertools import combinations

heights = [int(input()) for _ in range(9)]
for combi in combinations(heights, 7):
    if sum(combi) ==100:
        for i in sorted(combi):
            print(i)
        break


########## 방법2
# heights = [int(input()) for _ in range(9)]
# heights.sort()
# tot = sum(heights)
#
# def f():
#     for i in range(8):
#         for j in range(i + 1, 9):
#             if tot - heights[i] - heights[j] ==100:
#                 for k in range(9):
#                     if i!=k and j!=k:
#                         print(heights[k])
#
#                 return
#
#
# f()