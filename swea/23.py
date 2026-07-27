"""
서로 다른 한 자리 숫자들이 주어질 때, 이 숫자들을 모두 사용해서 만들 수 있는 가장 작은 수를 출력하세요.
[입력]
첫 번째 줄: 숫자 개수 N (2 ≤ N ≤ 4)
두 번째 줄: N개의 서로 다른 한 자리 숫자 (공백으로 구분)
[출력]
만들 수 있는 가장 작은 수
[제약사항]
sort() 메서드 사용
"""

N = int(input())
while True:
    arr = list(map(int, input().split()))

    if len(arr) == N:
        break
    print("다시 입력해주세요")

arr.sort()
# join 사용
print(''.join(map(str,arr)))

# for문 사용
result =''
for num in arr:
    result += str(num)
print(result)

# sep 사용
print(*arr, sep='')

# ---------------------------------------------------

# 강사님 풀이
n = int(input())
numbers = list(map(int, input().split()))

# 숫자들 오름차순 정렬
numbers.sort()

# 정렬된 숫자들을 이어붇이기('+')
result = ''
for num in numbers:     # iterator 방식 순회
    result += str(num)  # 문자열로 바꾼다

print(result)