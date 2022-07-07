#문제 : JadenCase 문자열 만들기

def solution(s):
    answer = s.split(" ");
    for i in range(len(answer)):
        answer[i] = answer[i].capitalize()
        
    return " ".join(answer)


print(solution("3people unFollowed me"))
print(solution("for the last week"))