#문제 : 이상한 문자 만들기

def solution(s):
    answer = ""
    cnt = 0
    for i in range(len(s)):
        if s[i] != " ":
            if cnt%2 == 0:
                answer += s[i].upper()
                cnt += 1
            else:
                answer += s[i].lower()
                cnt += 1
        else:
            answer += " "
            cnt = 0
    return answer

s = "try hello world"
s1 = "hello world try "

print(solution(s))
print(solution(s1))
