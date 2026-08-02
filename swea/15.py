"""
2중 for문을 사용하여 다음과 같이 출력해 보세요

1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
"""

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4]

for i in arr1:
    for j in arr2:
        print(i, j)

# 두번째 풀이(python for 문에서 자주 쓰는 변수명을 변경 / 리스트 선언하지 않고 range() 사용해 풀이)
for i in range(1,4):
    for j in range(1,5):
        print(i, j)

print()

# 강사님 풀이
for i in range(1, 3):       # 1 -> 2 -> 3
    for j in range(1,5):    # 1 -> 2 -> 3 -> 4
        print(i, j)

