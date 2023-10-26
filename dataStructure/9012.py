## 백준
# 9012번 괄호
# https://www.acmicpc.net/problem/9012



def is_valid_vps(s):
    stack = []
    result = True

    for char in s:
        if char == '(':
            stack.append(char)

        elif char == ')':
            if not stack:
                stack.append(char)
                break
            stack.pop()
    if not stack:
        result = True
    else:
        result = False

    print('YES' if result else 'NO')

T = int(input())
for X in range(T):
    input_string = input()
    is_valid_vps(input_string)

# 테스트 케이스 수 T를 입력 받음

# T = int(input())
# for _ in range(T):
#     stack = []
#     isVPS = True
#     for char in input():
#         if char == '(':
#             stack.append(char)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 isVPS=False
#                 break
#
#     if stack:
#         isVPS=False
#
#     print('YES' if isVPS else 'NO')