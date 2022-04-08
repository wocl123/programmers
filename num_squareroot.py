#문제 : 정수 제곱근 판별

def solution(n):
    answer = int(n**0.5)
    if answer**2 == n:
        return (answer+1)**2
    else:
        return -1

n1 = 121
n2 = 3

print(solution(n1))
print(solution(n2))