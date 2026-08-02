"""
리스트를 입력받고,
element 중 짝수가 하나라도 있으면 1, 없으면 0을 출력한다.

arr = list(map(int, input().split()))

flag = 0
for i in arr:
    if i % 2 == 0:
        flag = 1
        break

print(flag)
이 소스코드를 'flag처리' 라고 한다.

Q) 이 flag 처리 코드를 flag 변수를 쓰지 않고, 함수로 바꿔보자
힌트: for-break 대신 함수의 return 을 활용한다.
"""

arr = list(map(int, input().split()))

def func(arr):
    for i in arr:
        if i % 2 == 0:
            return 1
    return 0

print(func(arr)) 
    


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
