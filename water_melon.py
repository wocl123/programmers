#문제 : 수박수박수박수박수?

def solution(n):
    answer = ''
    
    for i in range(1, n+1):
        if i%2 != 0:
            answer += "수"
        else:
            answer += "박"
    return answer

n1 = 3
n2 = 4

print(solution(n1))
print(solution(n2))