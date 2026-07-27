# 내풀이
numbers = [0, 0, 0, 0, 0]

for i in range(len(numbers)):       # numbers 길이만큼의 range 함수 만듦 -> range(5) -> 0, 1, 2, 3, 4
    numbers[i] = 5 + i
    
for number in numbers:
    print(number, end=" ")

# 강사님 풀이
arr = [0, 0, 0, 0, 0]

x = 5
for i in range(5):
    arr[i] = x
    x += 1

print(*arr)
