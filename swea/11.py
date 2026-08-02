"""
num = 827364
1. 이 함수는 parameter 와 return 이 있습니다.
2. 이 함수의 기능은 prameter 의 짝수의 갯수와 홀수의 갯수를 return 합니다.

함수를 호출하고, 짝수의 갯수와 홀수의 갯수를 순서대로 출력 해 보세요.
단) for문 사용 금지, if 문 사용 금지

#출력결과
4
2
"""

num = 827364

def count(num):
    num = str(num)

    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    num4 = int(num[3])
    num5 = int(num[4])
    num6 = int(num[5])

# true 면 1 반환 되는것 사용
    even_num = (num1 % 2 == 0) + (num2 % 2 == 0) + (num3 % 2 == 0) + (num4 % 2 == 0) + (num5 % 2 == 0) + (num6 % 2 == 0)
    odd_num = 6 - even_num

    return even_num, odd_num

# a, b = x, y 형식 이용 (오른쪽 값을 왼쪽에 넣는거기때문에 = 기준 좌우 바뀌면 안됨)
even_num, odd_num = count(num)

print(even_num)
print(odd_num)