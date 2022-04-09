#문제 : 문자열 내림차순으로 배치하기

#첫번째 풀이
def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(ord(s[i]))
    answer.sort()
    result = []
    for i in range(len(answer)):
        result.append(chr(answer[i]))
    return "".join(result[::-1])

#두번째 풀이
def solution2(s):
    return "".join(sorted(s, reverse=True))

s1 = "Zbcdefg"
s2 = "BacGe"

print(solution2(s1))
print(solution2(s2))