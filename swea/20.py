"""
주어진 이메일 주소에서 도메인 부분만 추출하는 프로그램을 작성하세요.
[입력]
이메일 주소 하나 (예: user@gmail.com)
[출력]
도메인 부분만 출력 (예: gmail.com)
올바른 이메일 형식이 아니면 "Invalid email" 출력
[제약사항]
find() 메서드 사용
"""

# 함수 안에서 바로 print 로 하면 나중에 결과값을 재사용 못하니 return 으로 해서 값 내보내고 다른 변수에 함수 결과값 저장하고 그 변수를 프린트 하는게 좀 더 이상적인 방법
email = input()
n = email.find('@')

if n == -1:
    print("Invalid email")
else: print(email[n+1:])

def func(email):
    x = email.find('@')

    if x == -1:
        return "Invalid email"

    else: return email[x+1:]

result = func(email)
print(result)


T = input()
 
i = T.find('@')
 
if i == -1:
    print('Invalid email')
else:
    print(T[i+1:])

# 강사님 풀이
# 함수로 (월말 평가 이런식으로 함수 만드는 문제 나옴)
def extra_domain(email):
    # find 메서드로 @위치 찾기
    at_pos = email.find('@')

    # 만약 @ 없으면
    if at_pos == -1:
        return "Invalid email"

    # 만약 @ 있으면
    domain = email[at_pos + 1:]
    return domain

# 입력 받기
email = input()
result = extra_domain(email)
print(result)