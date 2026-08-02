"""
존재하는 단어, 각각 Counting
    - 배열에 들어있는 각 단어들 마다
      몇 개가 존재하는지 출력하는 프로그램 작성
        - Key 값 순회하기 방법을 사용해야함.
    - 입력예시
        MC BTS BTS MC BTS
    - 출력결과
        MC 2
        BTS 3
"""

arr = input().split()
d = dict()

for a in arr:
    d[a] = 0

for a in arr:
    d[a] += 1

for i in d:
    print(i, d[i])



# ------------------------------------------------------
# 강사님 풀이

arr = list(map(int, input().split()))

d = dict()
for a in arr:
    d[str(a)] = 0   # key 값의 value 0으로 초기화

for a in arr:
    d[str(a)] += 1  # counting

for i in d:         # 딕셔너리 key 를 기준으로 순회
    print(i, d[i])  # key value