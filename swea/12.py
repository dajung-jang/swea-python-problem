"""
- 이 함수는 팩토리얼 재귀함수 예시입니다.
def factorial(n):
	if n == 1:
    	return 1
	else: 
    	return n * factorial(n-1)
print(factorial(5))   # 120

1. argument 가 5로 함수호출되었을때 재귀 호출이 몇번 되었는지 출력합니다.
2. cnt 변수를 정의합니다.
3. global 키워드를 사용합니다.

Q) 이 문제의 경우 왜 global 키워드를 사용해야 할까요?

#출력결과
5
"""
cnt = 0

# 재귀 호출이 몇번됐는지 확인하려면 if, else 둘다 실행될때마다 count 를 올려야하기 때문에 상단에 +=1 구문 추가
def factorail(n):
    global cnt
    cnt += 1
    if n == 1:
        return 1

    else:
        return n * factorail(n-1)

factorail(5)
print(cnt)
            