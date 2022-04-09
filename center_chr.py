#문제 : 가운데 글자 가져오기

def solution(s):
    answer = ""
    if len(s)%2==0:
        answer += s[(len(s)//2)-1] + s[(len(s)//2)]
    else: 
        answer += s[(len(s))//2]
    return answer

s1 = "abcde"
s2 = "qwer"
s3 = "abcdefg"

print(solution(s1))
print(solution(s2))
print(solution(s3))