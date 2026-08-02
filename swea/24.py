"""
아래 배열을 하드코딩으로 초기화를 한다.
이후 한 문자열을 입력 받은 후,
배열 안에 입력 받은 문자열이 몇 개 존재하는지 출력한다.
    - 리스트에 없는 문자열은 입력되지 않는다.
    - Dictionary 를 이용하여 구현한다. (훈련을 위해 Count 함수 사용 금지)
ABC 77 -33 -33 125 ABC
-> {'ABC': 2, '77': 1, '-33': 2, '125': 1}
"""

arr = ['ABC', '77', '-33', '-33', '125', 'ABC']

d = dict()

for i in arr:
    d[str(i)] = 0

for i in arr:
    i = d[str(i)]
    str(i) += 1







# -------------------------------------------
# 강사님 풀이

# 리스트 index, element
# 딕셔너리 key, value

arr = ['ABC', 77, -33, -33, 125, 'ABC']

d = dict()
for a in arr:
    # 딕셔너리의 key로
    d[str(a)] = 0   #0으로 초기화

for a in arr:
    d[str(a)] += 1  # 카운팅

char = input()
print(d[char])  #value