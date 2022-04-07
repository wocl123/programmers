#문제 : 자릿수 더하기

def solution(n):
    st = str(n)
    sum = 0
    for i in range(len(st)):
        sum += int(st[i])
        
    return sum

n1 = 123
n2 = 987

print(solution(n1))
print(solution(n2))