#문제 : 3진법 뒤집기

def solution(n):
    answer = []
    sum = 0
    while(n != 0):
        answer.append(n%3)
        n = n // 3
    
    answer.reverse()
    for i in range(len(answer)):
        sum += answer[i] * (3**i)
    
    return sum

print(solution(45))
print(solution(125))