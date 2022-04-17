#문제 : 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
        if count%2 == 0:
            answer += i
        else:
            answer -= i
    return answer

left1 = 13
left2 = 24

right1 = 17
right2 = 27

print(solution(left1, right1))
print(solution(left2, right2))
