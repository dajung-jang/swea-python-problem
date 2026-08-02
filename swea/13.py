"""
- 섭씨 온도 변화식
C * 9/5 + 32

temps = [0, 20, 30, 37, 100]
1. 함수를 호출하면 화씨온도가 섭씨온도로 변환됩니다.
2. lambda 함수, map 함수 둘다 사용합니다.
3. 최종적으로 변환된 섭씨온도를 순서대로 출력합니다.

#출력결과
32.0 68.0 86.0 98.6 212.0
"""

temps = [0, 20, 30, 37, 100]

def func(arr):
    result = []
    for i in arr:
        result.append(i * 9/5 + 32)
    return result

print(*func(temps))