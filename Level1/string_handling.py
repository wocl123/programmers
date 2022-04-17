#문제 : 문자열 다루기 기본

def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else: 
        return False

print(solution("a234"))
print(solution("1234"))
print(solution("12345b"))
print(solution("12345677"))
