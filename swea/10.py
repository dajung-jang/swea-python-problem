"""
num = 12345
1. 이 함수는 parameter 와 return 이 있습니다.
2. 이 함수를 호출하면 숫자를 뒤집습니다.

#출력결과
54321
"""
num = "12345"

def func(x):
    return x[::-1]

print(func(num))