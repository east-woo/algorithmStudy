# 문제 설명
# 정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.
#
# "w" : 수에 1을 더한다.
# "s" : 수에 1을 뺀다.
# "d" : 수에 10을 더한다.
# "a" : 수에 10을 뺀다.
# 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.
#
# 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.
#
# 제한사항
# 2 ≤ numLog의 길이 ≤ 100,000
# -100,000 ≤ numLog[0] ≤ 100,000
# 1 ≤ i ≤ numLog의 길이인 모든 i에 대해 |numLog[i] - numLog[i - 1]|의 값은 1 또는 10입니다.
# 입출력 예
# numLog	result
# [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]	"wsdawsdassw"
# 입출력 예 설명
# 입출력 예 #1
#
# result인 "wsdawsdassw"를 따라 numLog[0]에서부터 시작해 조작을 하면 numLog의 값과 순서대로 일치합니다. 따라서 "wsdawsdassw"를 return 합니다.
# Hint
# "수 조작하기 1" 문제의 n값이 numLog[0]에 해당하며, 이 문제에서 주어진 numLog에 따라 "수 조작하기 1" 문제의 control을 구하는 문제라고 이해할 수 있습니다.
#
# 입출력 예 #1은 "수 조작하기 1" 문제의 입출력 예 #1과 같은 예시이므로 참고하시기 바랍니다.


def solution(numLog):
    answer = ''
    keyboard = {1:"w",
                -1:"s",
                10:"d",
                -10:"a"}

    for num in numLog:


    return answer

print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))