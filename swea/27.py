# 로또 번호 6개가 입력됩니다. 입력된 번호가 유효한 로또 번호인지 검증하세요. 유효한 로또 번호의 조건은 다음과 같습니다.
# 1. 6개의 서로 다른 번호
# 2. 각 번호는 1부터 45 사이의 정수
# [입력]
# 한 줄에 6개의 정수가 공백으로 구분되어 입력됩니다.
# [출력]
# 유효한 로또 번호이면 "VALID"를 출력하고, 그렇지 않으면 "INVALID"를 출력합니다
# [제약사항]
# add() 메서드 사용

numbers = list(map(int, input().split()))

unique_numbers = set()
is_duplicate = False

for num in numbers:
    if num in unique_numbers:
        is_duplicate = True
    unique_numbers.add(num)

is_in_range = True
for num in numbers:
    if num < 1 or num > 45:
        is_in_range: False

if not is_duplicate and is_in_range and len(numbers) == 6:
    print("VALID")
else: print("INVALID")

# ------------------------------------------------------
# 강사님 풀이

numbers = list(map(int, input().split()))

# 우선순위 1순위
if len(numbers) != 6:
    print("INVALID")

else: #길이가 6 인 경우
    lotto_set = set()
    for num in numbers:
        if 1 <= num <= 45:
            lotto_set.add(num)
    if len(lotto_set) == 6:     #로또의 숫자 개수가 6개
        print('VALID')
    else:                       # 로또의 숫자 개수가 6개 안될때
        print('INVALID')