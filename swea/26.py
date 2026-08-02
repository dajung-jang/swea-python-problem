"""
다음 딕셔너리를 하드코딩합니다.
scores = {
    'bogeom': 89,
    'sangho': 100,
    'IU': 78,
    'sori': 76,
    'hejun': 85
}
Q) 학생들의 시험 점수가 딕셔너리로 주어집니다.
   가장 높은 점수를 받은 학생의 이름을 출력하세요.

items()메서드 사용
"""

scores = {
    'bogeom': 89,
    'sangho': 100,
    'IU': 78,
    'sori': 76,
    'hejun': 85
}

max_v = 0
max_name =''

for name, score in scores.items():
    if score > max_v:
        max_v = score
        max_name = name

print(max_name)


# ---------------------------------------------------
# 강사님 풀이

scores = {
    'bogeom': 89,
    'sangho': 100,
    'IU': 78,
    'sori': 76,
    'hejun': 85
}
# 초기화
max_v = 0
best_student = ""

for name, score in scores.item():
    # 100% 최댓값 코드 구현 월말평가 나옴
    if score > max_v:
        max_v = score           # 갱신
        best_student = name     # 최대값 갱신 될 때의 학생

print(best_student)