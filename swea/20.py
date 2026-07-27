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