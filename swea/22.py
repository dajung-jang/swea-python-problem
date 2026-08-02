"""
선입선출 : 먼저들어온게(append), 먼저나간다(pop(0))
이 알고리즘을 큐(queue)라고 한다.
3명의 친구가 1, 2, 3번 순서로 원형으로 앉아있습니다. 맨 앞 친구가 맨 뒤로 이동하는 것을 N번 반복한 후, 맨 앞에 있는 친구의 번호를 출력하세요.
[입력]
이동 횟수 N (1 ≤ N ≤ 5)
[출력]
N번 이동 후 맨 앞에 있는 친구의 번호
[제약사항]
append() 메서드와, pop(0) 메서드 사용
"""
arr = [1, 2, 3]

while True:
    n = int(input())
    if n < 1 or n > 5:
        print("1이상 5이하의 정수로 다시 입력해주세요")
    else: break

for _ in range(n):
    i = arr.pop(0)
    arr.append(i)

result = arr[0]
print(result)

# 함수로 작성하면 이렇게
def func(arr):
    for _ in range(n):
        i = arr.pop(0)
        arr.append(i)
    return arr

print(func(arr))

arr = [1, 2, 3]
while True:
    N = int(input())
    if 1 <= N <= 5:
        break
        print("1 이상 5 이하의 정수로 다시 입력해주세요")
    
for _ in range(N):
    arr.append(arr.pop(0))

print(arr[0])

# --------------------------------------------------

# 강사님 풀이

n = int(input())

# 친구들 순서대로 넣기
friends = []
friends.append(1)
friends.append(2)
friends.append(3)

# N번 자리 바꾸기
for i in range(n):
    # 맨 앞에 친구 빼서(선출)
    front = friends.pop(0)
    # 맨 뒤에 추가(선입)
    friends.append(front)
# 맨 앞 친구 출력
print(friends[0])