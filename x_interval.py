#문제 : x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    sum = 0
    for i in range(n):
        sum += x
        answer.append(sum)
    return answer

x1 = 2
x2 = 4
x3 = -4

n1 = 5
n2 = 3
n3 = 2

print(solution(x1, n1))
print(solution(x2, n2))
print(solution(x3, n3))