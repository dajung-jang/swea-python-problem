# 내 풀이

# 첫 풀이
A = [1, 2, 3]
B = [1, 2, 3, 4]
for a in A:
  for b in B:
       print(a, b)

print() #줄바꿈

# 두번째 풀이(python for 문에서 자주 쓰는 변수명을 변경 / 리스트 선언하지 않고 range() 사용해 풀이)
for i in range(1,4):
    for j in range(1,5):
        print(i, j)

print()

# 강사님 풀이
for i in range(1, 3):       # 1 -> 2 -> 3
    for j in range(1,5):    # 1 -> 2 -> 3 -> 4
        print(i, j)

