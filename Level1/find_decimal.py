#문제 : 소수 찾기(Hint : 에라토스테네스의 체)

def solution(n):
    num = [True]*(n+1)
    sqrt = int(n**0.5)
    answer = 0
    for i in range(2, sqrt+1):
        if num[i] == False:
            continue
        
        for j in range(i+i, n+1, i):
            num[j] = False
    for i in range(2, n+1):
        if num[i] == True:
            answer += 1
    return answer

n1 = 10
n2 = 5

print(solution(n1))
print(solution(n2))
