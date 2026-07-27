"""
주어진 문자열을 반복 출력하는 StringRepeater 클래스를 작성하시오. 
클래스에는 반복 횟수와 문자열을 인자로 받아 문자열을 반복 출력하는 repeat_string 메서드가 포함되어야 한다.

- 실행 결과 
Hello
Hello
Hello
"""

# 아래 클래스를 수정하시오.
class StringRepeater:

    def repeat_string(self, n, word):
        for i in range(n):
            print(word)
    
repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

# 더 많이 쓰는 방식
"""
class StringRepeater:
    def __init__(self, n, word):
        self.n = n
        self.word = word

    def repeat_string(self):
        for i in range(self.n):
            print(self.word)

repreater1 = StringRepeater(3, 'Hello')
repeater1.repeat_string()
"""