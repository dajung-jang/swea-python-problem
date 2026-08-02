"""
리스트 1개를 입력받습니다.

1. 리스트의 element 중 최대값을 구합니다.
2. 그 element 의 index 를 출력합니다.
3. enumerate 내장함수를 사용합니다.
"""

arr = list(map(int, input().split()))

max_index = 0
max = arr[0]
for i, j in enumerate(arr):
    if j > max:
        max = j
        max_index = i

print(max_index)

# 내장함수 안쓰면

for x in range(len(arr)):
    if arr[x] > max:
        max = arr[x]
        max_index = x
print(max_index)


# 내 코드

arr = list(map(int, input().split()))

max_value = arr[0]
max_index = 0

for i, y in enumerate(arr):
    if y> max_value:
        max_value = y
        max_index = i

print(max_index)

# ==================================================
# 강사님 코드

# ** 문제에서 입력되는 숫자가 무조건 정수(양수)라는 조건이 없음 -> 음수 일수도 있다는 말

arr = list(map(int, input().split()))

# 초기화
max_v = float('-inf')   # 음의 무한대

for index, element in arr:
    if element > max.v:
        # max_v 를 계속 더 큰 값 나올때 마다 갱신
        max_v = element
        max_idx = index     # 최대값 나올 때의 인덱스
print(max_idx)




"""
월말평가
(9~12문제)
모든 문제 다 함수로 만들어야함
내장함수를 못씀 로직으로 짤 수 있어야함
sw 에서 Learn -> course에서 im형, a형, b형 (d어려울거여서 비기너 보면 좋을듯)

과목평가
객관식, 주관식, 서술형 -> pdf 에서 나옴

"""