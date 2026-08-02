"""
1. 문자열을 먼저 초기화 한다.
char = "Hello World"
2. 문자열에서 맨 앞과 맨 끝 알파벳 출력
3. 그 다음줄에 문자열에서 홀수 번째만 출력해 보기
4. 그 다음줄에 문자열에서 거꾸로 출력해 보기
"""
char = "Hello World"
print(char[0], char[-1])
print(char[::2])
print(char[::-1])