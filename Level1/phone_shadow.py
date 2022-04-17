#문제 : 핸드폰 번호 가리기

def solution(phone_number):
    answer = list(phone_number)
    for i in range(len(answer)-4):
        answer[i] = '*'
    return "".join(answer)

phone_number1 = "01033334444"
phone_number2 = "027778888"

print(solution(phone_number1))
print(solution(phone_number2))
