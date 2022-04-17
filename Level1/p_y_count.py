#문제 : 문자열 내 p와 y의 개수

#첫번째 풀이
def solution(s):
    answer = s.lower()
    p_y = [0,0]
    for i in answer:
        if i=='p': p_y[0] += 1
        if i=='y': p_y[1] += 1

    return p_y[0] == p_y[1]

#두번째 풀이
def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

s1 = "pPoooyY"
s2 = "Pyy"

print(solution2(s1))
print(solution2(s2))
