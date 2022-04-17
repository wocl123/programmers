#문제 : 피보나치 수

def fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo

def solution(n):
    answer = fibonacci(n)
    
    return answer[-1] % 1234567

print(solution(3))
print(solution(5))
print(solution(6))