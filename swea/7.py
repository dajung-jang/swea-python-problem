"""
range 활용하기
1. 0부터 4까지 출력 (5번 반복하는 반복문)
2. 3부터 12까지 3의 배수 출력
3. 20부터 -10까지 5의 배수 출력
"""
# range 는 슬라이싱이랑 다르게 , 로 구분 (슬라이싱은 : 로 구분)

print(*list(range(5)))
print(*list(range(3, 13, 3)))
print(*list(range(20, -11, -5)))

#-------------------------------------------------
# 추가 메모

# range() vs map()
r = range(5)
print(r)    # range(0, 5) => 리스트 아님

# 인덱싱 가능
print(r[2])     # 2

# len()사용 가능
print(len(r))   # 5

#  슬라이싱 가능
r2 = r[2:5]
print(list(r2)) #[2, 3, 4]

print(3 in r)   # True

# for문에서는 list() 없이도 바로 사용 가능
for i in r:
    print(i)

#---------
# map 은 한번 순회하면 못씀 -> 결과 여러번 쓰거나 인젣스로 접근하고 싶으면 list 로 감싸줘야함
m = map(str, [1, 2, 3])
print(m)    # <map object at 0.....> => 인덱싱 불가능
# print(m[0])   # 에러남
# print(len(m)) # 에러남

for x in m:
    print(x)

for x in m: 
    print(x)    # 아무것도 안나옴 (이미 소진됨)