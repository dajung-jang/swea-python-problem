"""
운년의 조건은 다음과 같다
- 1. 4로 나누어 떨어지고, 100으로는 나누어 떨어지지 않는다
- 2. 400으로 나누어떨어진다.
정수를 입력받고
윤년이면 1을 출력하고, 평년이면 0을 출력해 보자
"""

n = int(input())

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(1)
else: print(0)


# # 강사님 풀이

# n = int(input())

# if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0: print(1)
# else: print(0)

# # 내 풀이

# T = int(input())
 
# if (T % 4 == 0 and T % 100 != 0) or T % 400 == 0 :
#     print(1)
# else:
#     print(0)

