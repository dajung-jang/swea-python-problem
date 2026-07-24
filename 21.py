"""
후입선출 : 나중에 들어온게(append), 먼저나간다(pop)
이 알고리즘을 스택(stack)이라고 한다.


정수들이 하나씩 주어질 때, 0이 나오면 지금까지 입력된 정수들을 역순으로 출력하는 프로그램을 작성하세요.

 

[입력]

여러 줄에 걸쳐 정수 하나씩 입력

마지막에 "0" 입력
 
[출력]

입력된 정수들을 역순으로 이어붙인 단어

[제약사항]

append() 메서드와 pop() 메서드 사용
"""
numbers = []

while True:
	n = int(input())
	if n == 0:
		break
	numbers.append(n)

while numbers:
    print(numbers.pop(), end='')

# 강사님 풀이
stack =[]

while True:
    num = int(input())

    if num == 0:
        break

    # 입력받은 문자 스택에 추가
    stack.append(num)

# 스택에서 하나씩 빼면서(후입선출) 단어 만들기
word = ""
while len(stack) > 0:
    word += str(stack.pop())

print(word)

