#  내 풀이

def has_even(arr):
    for i in arr:
        if i %2 == 0:
            return 1
    return 0

arr = list(map(int, input().split()))     # 입력받은 데이터를 공백을 기준으로 분리 -> 정수로 변경 -> 리스트 형변환

print(has_even(arr))

# 강사님 풀이

arr = list(map(int, input().split()))

def is_even(arr):
    for i in arr:                   # iterator 방식으로 순회
        if i % 2 == 0: return 1     # 짝수면 1 반환하고 함수 종료
    return 0                        # 짝수가 하나라도 없으면 0 반환하고 함수 종료

print(is_even(arr))
