"""
- 먼저 0 으로 채워진 5칸으로 구성된 리스트를 만든다.
- 이후 for문을 이용하여 모든 칸을 5에서 하나씩 더한 값으로 채운다
- 이후 for문으로 순회하며 모든 값을 하나씩 출력해본다.
0 0 0 0 0
5 6 7 8 9
"""

arr = [0, 0, 0, 0, 0]

for i in range(5):
    arr[i] = 5 + i

for j in arr:
    print(j, end=" ")

# # 내풀이
# numbers = [0, 0, 0, 0, 0]

# for i in range(len(numbers)):       # numbers 길이만큼의 range 함수 만듦 -> range(5) -> 0, 1, 2, 3, 4
#     numbers[i] = 5 + i
    
# for number in numbers:
#     print(number, end=" ")

# # 강사님 풀이
# arr = [0, 0, 0, 0, 0]

# x = 5
# for i in range(5):
#     arr[i] = x
#     x += 1

# print(*arr)
