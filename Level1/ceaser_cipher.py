def solution(s, n):
    answer = list(s)
    for i in range(len(answer)):
        if answer[i].isupper():
            answer[i] = chr((ord(answer[i]) - ord('A') + n)%26 +ord('A'))
        elif answer[i].islower():
            answer[i] = chr((ord(answer[i]) - ord('a') + n)%26 + ord('a'))
                
    return "".join(answer)

s1 = "AB"
s2 = "z"
s3 = "a B z"

n1 = 1
n2 = 1
n3 = 4

print(solution(s1, n1))
print(solution(s2, n2))
print(solution(s3, n3))

#a~z = 97 ~ 122 (25차이)
#A~Z = 65 ~ 90 (25차이)

# 97 122
